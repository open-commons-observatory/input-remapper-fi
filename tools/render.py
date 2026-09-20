"""Render Markdown pages from the database using SQL files + Jinja templates (see docs/pages.yaml).
Deterministic: the same database commit and templates give byte-identical output (no timestamps).
A page with `for_each` is rendered once per row of that query; every column of the row is bound as a
query parameter (%(column)s), usable in `out` paths ({column}) and available to the template as `row`."""
import pathlib, shutil, types, yaml, jinja2

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"


def cell(s, n=None):
    s = " ".join(str(s if s is not None else "").split()).replace("|", "\\|")
    return s if not n or len(s) <= n else s[: n - 1].rstrip() + "…"


def render(conn, out, cfg, write_mkdocs=True):
    spec = yaml.safe_load((DOCS / "pages.yaml").read_text())
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(DOCS / "templates"), trim_blocks=True, lstrip_blocks=True,
                             keep_trailing_newline=True, undefined=jinja2.StrictUndefined)
    env.filters["cell"] = cell
    vars_ = {"title": cfg["title"], "tagline": cfg["tagline"], "name": cfg["name"], "repo": cfg["repo"],
             "source": cfg["source"]["repo"], "pie_facet": cfg.get("pie_facet")}

    def q(name, params=None):
        # Rows become namespaces, not dicts: in Jinja `row.items` on a dict is the dict METHOD, not a column
        # called "items" (same for keys, values, get, ...). Namespaces have no such methods.
        rows = conn.execute((DOCS / "queries" / name).read_text(), params or {}).fetchall()
        return [types.SimpleNamespace(**r) for r in rows]

    if out.exists():
        shutil.rmtree(out)          # stale pages must disappear when their data disappears
    written = 0
    for page in spec["pages"]:
        tpl = env.get_template(page["template"])
        jobs = [vars(r) for r in q(page["for_each"]["query"])] if "for_each" in page else [{}]
        for row in jobs:
            ctx = {k: q(f, row) for k, f in page["queries"].items()}
            target = out / page["out"].format(**row)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(tpl.render(vars=vars_, row=types.SimpleNamespace(**row), param=next(iter(row.values()), None), **ctx), encoding="utf-8")
            written += 1
    if write_mkdocs:
        (ROOT / "mkdocs.yml").write_text(env.get_template("mkdocs.yml.j2").render(vars=vars_), encoding="utf-8")
    print(f"rendered {written} pages into {out}")
