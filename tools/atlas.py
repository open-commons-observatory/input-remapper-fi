#!/usr/bin/env python3
"""atlas: acquire -> read -> tag -> validate -> render, on a version-controlled Postgres-compatible
database (Doltgres). One tool, one config (atlas.yaml), one vocabulary (taxonomy.yaml).

  atlas db up|down|init|pull|push  manage the database server and its copy in GitHub (refs/dolt/data)
  atlas acquire                  fetch issues, PRs and commits from GitHub into the database
  atlas next [-n 12]             which unread items come next (state lives in the database)
  atlas read N [N...]            print threads to read (API, never HTML)
  atlas apply BATCH.tsv          validate a whole batch, then write it atomically and commit
  atlas status | check           coverage numbers computed now; quality warnings
  atlas export                   deterministic CSV of every table into data/ (reviewable on GitHub)
  atlas render                   render Markdown pages from SQL + templates
  atlas sql "SELECT ..."         run any SQL (add --commit MSG to record a change)
"""
import argparse, base64, csv, json, os, pathlib, re, shutil, subprocess, sys, time
import urllib.error, urllib.parse, urllib.request

import psycopg
import yaml
from psycopg import sql
from psycopg.rows import dict_row

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

TABLE_KEYS = {  # deterministic export order
    "facet": ["name"], "facet_value": ["facet", "value"], "item": ["n"], "git_commit": ["sha"],
    "analysis": ["item_n"], "tag": ["item_n", "facet", "value"], "problem": ["id"],
    "problem_item": ["problem_id", "item_n"],
}


# ---------------------------------------------------------------- config / connection
def cfg():
    c = yaml.safe_load((ROOT / "atlas.yaml").read_text())
    if os.environ.get("ATLAS_REPO"):
        c["repo"] = os.environ["ATLAS_REPO"]
    if os.environ.get("ATLAS_DATABASE"):      # tests use a private database on a shared server
        c["database"] = os.environ["ATLAS_DATABASE"]
    return c


def home():
    return pathlib.Path(os.environ.get("ATLAS_HOME") or pathlib.Path.home() / ".cache" / "oco-atlas" / cfg()["name"])


def dsn(dbname):
    return dict(host=os.environ.get("PGHOST", "127.0.0.1"), port=os.environ.get("PGPORT", "5432"),
                user=os.environ.get("PGUSER", "postgres"), password=os.environ.get("PGPASSWORD", "password"),
                dbname=dbname)


def connect(dbname=None):
    return psycopg.connect(**dsn(dbname or cfg()["database"]), row_factory=dict_row, autocommit=True)


def server_up():
    try:
        psycopg.connect(**dsn("postgres"), connect_timeout=2).close()
        return True
    except psycopg.OperationalError:
        return False


def die(msg):
    sys.exit(f"atlas: {msg}")


# ---------------------------------------------------------------- database helpers
def upsert(conn, table, key, row):
    """SELECT-then-UPDATE/INSERT: portable, and does not depend on how rowcount treats unchanged rows."""
    where = " AND ".join(f"{k}=%({k})s" for k in key)
    exists = conn.execute(f"SELECT 1 FROM {table} WHERE {where}", row).fetchone()
    rest = [k for k in row if k not in key]
    if exists:
        if rest:
            conn.execute(f"UPDATE {table} SET " + ", ".join(f"{k}=%({k})s" for k in rest) + f" WHERE {where}", row)
        return "updated"
    conn.execute(f"INSERT INTO {table} ({', '.join(row)}) VALUES ({', '.join(f'%({k})s' for k in row)})", row)
    return "inserted"


def commit(conn, msg):
    conn.execute("SELECT dolt_add('.')")
    try:
        conn.execute(sql.SQL("SELECT dolt_commit('-m', {})").format(sql.Literal(msg)))
    except psycopg.Error as e:
        if "nothing to commit" in str(e).lower():
            print("(no changes to commit)")
            return False
        raise
    print(f"committed: {msg}")
    return True


def run_sql_file(conn, path):
    for stmt in re.split(r";[ \t]*\n", pathlib.Path(path).read_text()):
        body = "\n".join(l for l in stmt.splitlines() if not l.strip().startswith("--")).strip()
        if body:
            conn.execute(body)


def taxonomy():
    t = yaml.safe_load((ROOT / (os.environ.get("ATLAS_TAXONOMY") or cfg().get("taxonomy", "taxonomy.yaml"))).read_text())["facets"]
    for name, f in t.items():
        for v in f["values"]:
            if not isinstance(v, str):
                die(f"taxonomy: value {v!r} of facet {name!r} is not a string (YAML turns yes/no/on/off into booleans; quote it)")
    return t


def taxonomy_from_db(conn):
    tax = {r["name"]: {"multi": r["multi"], "values": {}} for r in conn.execute("SELECT name, multi FROM facet").fetchall()}
    for r in conn.execute("SELECT facet, value, doc FROM facet_value").fetchall():
        tax[r["facet"]]["values"][r["value"]] = r["doc"]
    return tax


def taxonomy_drift(conn):
    """Differences between taxonomy.yaml and what the database holds (empty list = in sync)."""
    yml, db, out = taxonomy(), taxonomy_from_db(conn), []
    for f in sorted(set(yml) | set(db)):
        if f not in db:
            out.append(f"facet {f!r} is in taxonomy.yaml but not in the database")
        elif f not in yml:
            out.append(f"facet {f!r} is in the database but not in taxonomy.yaml")
        else:
            for v in sorted(set(yml[f]["values"]) ^ set(db[f]["values"])):
                where = "taxonomy.yaml only" if v in yml[f]["values"] else "database only"
                out.append(f"value {f}:{v} is in {where}")
            if bool(yml[f].get("multi")) != bool(db[f]["multi"]):
                out.append(f"facet {f!r}: multi differs between taxonomy.yaml and the database")
    return out


def taxonomy_sync(conn):
    t = taxonomy()
    for name, f in t.items():
        upsert(conn, "facet", ["name"], {"name": name, "multi": bool(f.get("multi")), "page": bool(f.get("page")), "doc": f.get("doc", "")})
        for val, doc in f["values"].items():
            upsert(conn, "facet_value", ["facet", "value"], {"facet": name, "value": val, "doc": doc or ""})
    for r in conn.execute("SELECT facet, value FROM facet_value").fetchall():
        if r["facet"] not in t or r["value"] not in t[r["facet"]]["values"]:
            n = conn.execute("SELECT count(*) AS n FROM tag WHERE facet=%s AND value=%s", (r["facet"], r["value"])).fetchone()["n"]
            if n:
                die(f"taxonomy: {r['facet']}:{r['value']} was removed but {n} tags use it; retag those first")
            conn.execute("DELETE FROM facet_value WHERE facet=%s AND value=%s", (r["facet"], r["value"]))
    for r in conn.execute("SELECT name FROM facet").fetchall():
        if r["name"] not in t:
            conn.execute("DELETE FROM facet WHERE name=%s", (r["name"],))


# ---------------------------------------------------------------- db up / init / pull / push
def cmd_db_up(a=None):
    if server_up():
        print("database server already running")
        return
    binp = os.environ.get("DOLTGRES_BIN") or shutil.which("doltgres")
    if not binp:
        die("doltgres not found; run tools/install-doltgres.sh (or set DOLTGRES_BIN)")
    h = home()
    (h / "data").mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:  # lets the server push to / clone from GitHub without touching global git config
        env.update(GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
                   GIT_CONFIG_VALUE_0="Authorization: Basic " + base64.b64encode(f"x-access-token:{tok}".encode()).decode())
    log = open(h / "server.log", "ab")
    # cwd outside the repo: Doltgres writes .doltcfg/ (auth databases) into its working directory.
    proc = subprocess.Popen([binp, "-data-dir", str(h / "data")], cwd=h, stdout=log, stderr=log, env=env, start_new_session=True)
    (h / "server.pid").write_text(str(proc.pid))
    for _ in range(60):
        if server_up():
            print("database server up")
            return
        time.sleep(0.5)
    die(f"server did not start; see {h / 'server.log'}")


def cmd_db_down(a=None):
    """Stop the server that `atlas db up` started. Restart it after exporting GITHUB_TOKEN if push or clone needs credentials."""
    import signal
    pidfile = home() / "server.pid"
    if not pidfile.exists():
        die(f"no {pidfile}; the server was not started by atlas. Stop the doltgres process yourself.")
    try:
        os.kill(int(pidfile.read_text()), signal.SIGTERM)
    except ProcessLookupError:
        pass
    for _ in range(40):
        if not server_up():
            break
        time.sleep(0.25)
    pidfile.unlink(missing_ok=True)
    print("database server stopped" if not server_up() else "server still answering; stop it manually")


def db_exists(name):
    with connect("postgres") as c:
        return bool(c.execute("SELECT 1 FROM pg_database WHERE datname=%s", (name,)).fetchone())


def cmd_db_init(a=None):
    cmd_db_up()
    name = cfg()["database"]
    if not db_exists(name):
        with connect("postgres") as c:
            c.execute(f'CREATE DATABASE "{name}"')
    with connect() as conn:
        try:
            conn.execute("SELECT 1 FROM item LIMIT 1")
        except psycopg.Error:
            run_sql_file(conn, ROOT / "db" / "schema.sql")
            print("schema created")
        taxonomy_sync(conn)
        commit(conn, "init: schema and taxonomy")


def repo_url():
    return f"https://github.com/{cfg()['repo']}.git"


def cmd_db_pull(a=None):
    cmd_db_up()
    name = cfg()["database"]
    if db_exists(name):
        with connect() as conn:
            conn.execute("SELECT dolt_pull('origin', 'main')")
        print("database updated from", repo_url())
    else:
        with connect("postgres") as c:
            c.execute(sql.SQL("SELECT dolt_clone({}, {})").format(sql.Literal(repo_url()), sql.Literal(name)))
        print("database cloned from", repo_url())


def cmd_db_push(a=None):
    with connect() as conn:
        remotes = [r["name"] for r in conn.execute("SELECT name FROM dolt_remotes").fetchall()]
        if "origin" not in remotes:
            conn.execute(sql.SQL("SELECT dolt_remote('add', 'origin', {})").format(sql.Literal(repo_url())))
        try:
            out = conn.execute("SELECT dolt_push('origin', 'main')").fetchone()
        except psycopg.Error as e:
            msg = str(e).splitlines()[0]
            hint = ("\n  The server was probably started without GITHUB_TOKEN. Export it, then run `atlas db down` and `atlas db up`, and push again."
                    if "Username" in str(e) or "credential" in str(e).lower() else "")
            die(f"database push FAILED, GitHub does not have your latest data: {msg}{hint}")
        print("pushed database to", repo_url())
        print(list(out.values())[0])


# ---------------------------------------------------------------- GitHub API
def gh(path, params=None):
    url = "https://api.github.com" + path + ("?" + urllib.parse.urlencode(params) if params else "")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "oco-atlas"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and e.headers.get("X-RateLimit-Remaining") == "0":
                wait = max(1, int(e.headers.get("X-RateLimit-Reset", "0")) - int(time.time()))
                die(f"GitHub rate limit exhausted; resets in {wait}s (set GITHUB_TOKEN for 5000/hour)")
            if e.code >= 500 and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            die(f"GitHub API {e.code} for {path}")


def paginate(path, params=None):
    page = 1
    while True:
        data = gh(path, {**(params or {}), "per_page": 100, "page": page})
        yield from data
        if len(data) < 100:
            return
        page += 1


def item_row(x):
    pr = "pull_request" in x
    merged = pr and bool((x["pull_request"] or {}).get("merged_at"))
    closed = x.get("closed_at")
    return {"n": x["number"], "title": x["title"], "is_pr": pr, "state": "MERGED" if merged else x["state"].upper(),
            "created": x["created_at"][:10], "closed": closed[:10] if closed else None,
            "author": (x.get("user") or {}).get("login") or "ghost", "comments": x["comments"],
            "labels": ",".join(sorted(l["name"] for l in x.get("labels", [])))}


def commit_row(x):
    return {"sha": x["sha"], "subject": (x["commit"]["message"].splitlines() or [""])[0][:300] or "(no subject)",
            "author": (x["commit"]["author"] or {}).get("name") or "unknown", "committed": x["commit"]["author"]["date"][:10]}


def cmd_acquire(a):
    src = cfg()["source"]["repo"]
    cmd_db_up()
    with connect() as conn:
        if a.items_json:
            items = json.load(open(a.items_json))
        elif a.commits_only:
            items = []
        else:
            print(f"fetching issues and PRs of {src} ...")
            items = list(paginate(f"/repos/{src}/issues", {"state": "all", "sort": "created", "direction": "asc"}))
        counts = {"inserted": 0, "updated": 0}
        with conn.transaction():
            for x in items:
                counts[upsert(conn, "item", ["n"], item_row(x))] += 1
        print(f"items: {counts['inserted']} new, {counts['updated']} refreshed")
        commits = []
        if a.commits_json:
            commits = json.load(open(a.commits_json))
        elif not (a.items_json or a.items_only):
            print(f"fetching commits of {src} ...")
            commits = list(paginate(f"/repos/{src}/commits"))
        cc = {"inserted": 0, "updated": 0}
        with conn.transaction():
            for x in commits:
                cc[upsert(conn, "git_commit", ["sha"], commit_row(x))] += 1
        print(f"commits: {cc['inserted']} new, {cc['updated']} refreshed")
        commit(conn, f"acquire: {counts['inserted']} new items, {cc['inserted']} new commits")


# ---------------------------------------------------------------- reading
def clip(s, n):
    s = (s or "").strip()
    return s if len(s) <= n else s[:n].rstrip() + " [..cut]"


def cmd_read(a):
    c = cfg()
    src, maint = c["source"]["repo"], set(c["source"].get("maintainers", []))
    for n in a.numbers:
        it = gh(f"/repos/{src}/issues/{n}")
        print(f"=== #{n} [{it['created_at'][:10]}] {it['title']}  ({'PR' if 'pull_request' in it else 'issue'}, {it['state']}, comments {it['comments']})")
        print("Q:", clip(it.get("body"), a.q))
        got = skipped = 0
        for cm in paginate(f"/repos/{src}/issues/{n}/comments"):
            got += 1
            who = (cm.get("user") or {}).get("login") or "ghost"
            is_m = who in maint
            body = clip(cm["body"], a.cap if is_m else a.users)
            if not is_m and len(body) < a.min:
                skipped += 1
                continue
            print(f"{'M' if is_m else 'u'}[{cm['created_at'][:10]}] {who}: {body}")
        note = f"[{got} comments fetched" + (f", {skipped} short user replies skipped" if skipped else "") + "]"
        if got != it["comments"]:
            note += f"  WARNING: GitHub reports {it['comments']} comments (hidden-text check failed)"
        print(note, "\n")


def cmd_next(a):
    kind = {"issue": "NOT i.is_pr", "pr": "i.is_pr", "any": "TRUE"}[a.kind]
    with connect() as conn:
        rows = conn.execute(f"SELECT i.n FROM item i WHERE {kind} AND NOT EXISTS (SELECT 1 FROM analysis a WHERE a.item_n = i.n) ORDER BY i.n LIMIT {int(a.count)}").fetchall()
    print(" ".join(str(r["n"]) for r in rows))


# ---------------------------------------------------------------- apply (atomic, validated batches)
def parse_batch(path, tax, item_ids):
    errors, rows = [], {}
    for ln, raw in enumerate(pathlib.Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        where = f"{pathlib.Path(path).name}:{ln}"
        parts = [p.strip() for p in raw.split(" | ", 3)]
        if len(parts) != 4:
            errors.append(f"{where}: expected 'iN | - | facet:value ... depth=full | summary'")
            continue
        m = re.fullmatch(r"i?(\d+)", parts[0])
        if not m:
            errors.append(f"{where}: bad item id {parts[0]!r}")
            continue
        n, depth, tags = int(m.group(1)), "full", set()
        if n not in item_ids:
            errors.append(f"{where}: item #{n} is not in the database (run `atlas acquire`)")
        if n in rows:
            errors.append(f"{where}: item #{n} appears twice in this batch")
        for tok in parts[2].split():
            if tok.startswith("depth="):
                depth = tok[6:]
                if depth not in ("title", "thread", "full", "source"):
                    errors.append(f"{where}: bad depth {depth!r}")
            elif ":" not in tok:
                errors.append(f"{where}: tag {tok!r} is not facet:value")
            else:
                f, v = tok.split(":", 1)
                if f not in tax:
                    errors.append(f"{where}: unknown facet {f!r} (facets: {', '.join(sorted(tax))})")
                elif v not in tax[f]["values"]:
                    errors.append(f"{where}: {f}:{v} is not in the taxonomy (allowed: {', '.join(tax[f]['values'])})")
                else:
                    tags.add((f, v))
        for f in {f for f, _ in tags if not tax[f].get("multi")}:
            vals = sorted(v for ff, v in tags if ff == f)
            if len(vals) > 1:
                errors.append(f"{where}: facet {f!r} is single-valued but has {vals}")
        if not parts[3]:
            errors.append(f"{where}: empty summary")
        rows[n] = {"depth": depth, "summary": parts[3], "tags": tags}
    return rows, errors


def apply_sql_batch(conn, a):
    """A .sql batch is a reviewable bulk edit (e.g. a re-tag). One transaction: the database's own constraints are the validator."""
    text = pathlib.Path(a.batch).read_text(encoding="utf-8")
    n = sum(1 for st in re.split(r";[ \t]*\n", text) if "\n".join(l for l in st.splitlines() if not l.strip().startswith("--")).strip())
    if a.dry_run:
        print(f"ok: {n} statements would be applied in one transaction")
        return
    try:
        with conn.transaction():
            run_sql_file(conn, a.batch)
    except psycopg.Error as e:
        print(f"REJECTED: {str(e).splitlines()[0]}; nothing was written", file=sys.stderr)
        sys.exit(1)
    print(f"applied {n} statements from {pathlib.Path(a.batch).name}")
    commit(conn, f"apply {pathlib.Path(a.batch).stem}: {n} statements")


def cmd_apply(a):
    with connect() as conn:
        drift = taxonomy_drift(conn)
        if drift:
            die("taxonomy.yaml and the database disagree; run `atlas db init` to load the file (or fix the file):\n  " + "\n  ".join(drift[:8]))
        if a.batch.endswith(".sql"):
            return apply_sql_batch(conn, a)
        tax = taxonomy_from_db(conn)
        ids = {r["n"] for r in conn.execute("SELECT n FROM item").fetchall()}
        stem = pathlib.Path(a.batch).stem
        batch = (re.match(r"\d+", stem) or re.match(r".*", stem)).group(0)
        rows, errors = parse_batch(a.batch, tax, ids)
        if errors:
            print(f"REJECTED: {len(errors)} problem(s); nothing was written", file=sys.stderr)
            for e in errors[:40]:
                print("  " + e, file=sys.stderr)
            sys.exit(1)
        if a.dry_run:
            print(f"ok: {len(rows)} items would be applied")
            return
        with conn.transaction():
            for n, r in sorted(rows.items()):
                upsert(conn, "analysis", ["item_n"], {"item_n": n, "batch": batch, "depth": r["depth"], "summary": r["summary"]})
                conn.execute("DELETE FROM tag WHERE item_n=%s", (n,))
                for f, v in sorted(r["tags"]):
                    conn.execute("INSERT INTO tag (item_n, facet, value) VALUES (%s, %s, %s)", (n, f, v))
        print(f"applied {len(rows)} items from {pathlib.Path(a.batch).name}")
        commit(conn, f"apply {stem}: {len(rows)} items")


# ---------------------------------------------------------------- status / check / export / render / sql
def cmd_status(a=None):
    with connect() as conn:
        for r in conn.execute("SELECT i.is_pr, count(*) AS total, count(a.item_n) AS analysed FROM item i LEFT JOIN analysis a ON a.item_n=i.n GROUP BY i.is_pr ORDER BY i.is_pr").fetchall():
            pct = 100 * r["analysed"] / r["total"] if r["total"] else 0
            print(f"{'pull requests' if r['is_pr'] else 'issues':14} {r['analysed']:>5} of {r['total']:<5} analysed ({pct:.0f}%)")
        depth = ", ".join(f"{r['depth']}={r['n']}" for r in conn.execute("SELECT depth, count(*) AS n FROM analysis GROUP BY depth ORDER BY depth").fetchall())
        print("depth:", depth or "(nothing analysed yet)")
        print("commits acquired:", conn.execute("SELECT count(*) AS n FROM git_commit").fetchone()["n"])
        last = conn.execute("SELECT substr(commit_hash,1,12) AS h, message FROM dolt_log LIMIT 1").fetchone()
        print(f"database commit: {last['h']} {last['message']}")


def cmd_check(a):
    c, warnings = cfg(), []
    with connect() as conn:
        warnings += [f"taxonomy drift: {d}" for d in taxonomy_drift(conn)]
        for f in c.get("required_facets", []):
            n = conn.execute("SELECT count(*) AS n FROM analysis a WHERE NOT EXISTS (SELECT 1 FROM tag t WHERE t.item_n=a.item_n AND t.facet=%s)", (f,)).fetchone()["n"]
            if n:
                warnings.append(f"{n} analysed items have no {f!r} tag")
        for r in conn.execute("SELECT facet, sum(CASE WHEN value='unknown' THEN 1 ELSE 0 END) AS u, count(*) AS n FROM tag GROUP BY facet").fetchall():
            if r["u"] and r["u"] * 4 >= r["n"]:
                warnings.append(f"facet {r['facet']!r}: {r['u']} of {r['n']} tags are 'unknown' ({100 * r['u'] // r['n']}%)")
    for w in warnings:
        print("WARN", w)
    print(f"{len(warnings)} warning(s)")
    if warnings and a.strict:
        sys.exit(1)


def cmd_export(a):
    out = pathlib.Path(a.dir or ROOT / "data")
    out.mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        for table, key in TABLE_KEYS.items():
            rows = conn.execute(f"SELECT * FROM {table} ORDER BY {', '.join(key)}").fetchall()
            with open(out / f"{table}.csv", "w", newline="", encoding="utf-8") as fh:
                w = csv.writer(fh, lineterminator="\n")
                cols = list(rows[0]) if rows else [d.name for d in conn.execute(f"SELECT * FROM {table} LIMIT 0").description]
                w.writerow(cols)
                for r in rows:
                    w.writerow(["" if r[c] is None else r[c] for c in cols])
    print(f"exported {len(TABLE_KEYS)} tables to {out}")


def cmd_render(a):
    import render
    with connect() as conn:
        render.render(conn, pathlib.Path(a.out) if a.out else ROOT / "docs" / "generated", cfg(), write_mkdocs=not a.out)


def cmd_sql(a):
    text = a.statement or sys.stdin.read()
    with connect() as conn:
        cur = conn.execute(text)
        if cur.description:
            rows = cur.fetchall()
            cols = [d.name for d in cur.description]
            width = {c: max([len(c)] + [len(str(r[c])) for r in rows]) for c in cols}
            print(" | ".join(c.ljust(width[c]) for c in cols))
            print("-+-".join("-" * width[c] for c in cols))
            for r in rows:
                print(" | ".join(str(r[c]).ljust(width[c]) for c in cols))
            print(f"({len(rows)} rows)")
        if a.commit:
            commit(conn, a.commit)


# ---------------------------------------------------------------- CLI
def main():
    p = argparse.ArgumentParser(prog="atlas", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    db = sub.add_parser("db", help="database server and its GitHub copy")
    dbs = db.add_subparsers(dest="sub", required=True)
    for name, fn in (("up", cmd_db_up), ("down", cmd_db_down), ("init", cmd_db_init), ("pull", cmd_db_pull), ("push", cmd_db_push)):
        dbs.add_parser(name).set_defaults(fn=fn)
    s = sub.add_parser("acquire", help="fetch issues, PRs, commits")
    s.add_argument("--items-only", action="store_true")
    s.add_argument("--commits-only", action="store_true")
    s.add_argument("--items-json", help="load items from a JSON file in GitHub API shape (offline/tests)")
    s.add_argument("--commits-json", help="load commits from a JSON file in GitHub API shape (offline/tests)")
    s.set_defaults(fn=cmd_acquire)
    s = sub.add_parser("next", help="next unread item numbers")
    s.add_argument("-n", "--count", type=int, default=12)
    s.add_argument("--kind", choices=["issue", "pr", "any"], default="issue")
    s.set_defaults(fn=cmd_next)
    s = sub.add_parser("read", help="print threads")
    s.add_argument("numbers", type=int, nargs="+")
    s.add_argument("--q", type=int, default=400, help="max chars of the opening post")
    s.add_argument("--cap", type=int, default=600, help="max chars per maintainer comment")
    s.add_argument("--users", type=int, default=250, help="max chars per user comment")
    s.add_argument("--min", type=int, default=60, help="skip user replies shorter than this")
    s.set_defaults(fn=cmd_read)
    s = sub.add_parser("apply", help="apply a batch file")
    s.add_argument("batch")
    s.add_argument("--dry-run", action="store_true")
    s.set_defaults(fn=cmd_apply)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    s = sub.add_parser("check")
    s.add_argument("--strict", action="store_true")
    s.set_defaults(fn=cmd_check)
    s = sub.add_parser("export")
    s.add_argument("--dir")
    s.set_defaults(fn=cmd_export)
    s = sub.add_parser("render")
    s.add_argument("--out", help="write pages here instead of docs/generated (skips mkdocs.yml)")
    s.set_defaults(fn=cmd_render)
    s = sub.add_parser("sql")
    s.add_argument("statement", nargs="?")
    s.add_argument("--commit", metavar="MSG")
    s.set_defaults(fn=cmd_sql)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
