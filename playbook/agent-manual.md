# Agent manual: environment, procedures and checks

For an AI agent (or a human) working on this repository. The entry point and the rules are in [AGENTS.md](../AGENTS.md); the reasons are in [decisions/](../decisions/) and [lessons](lessons.md).

## 1. The token

The owner provides a GitHub token at the start of each session. Put it **in the environment only** (`export GITHUB_TOKEN=...` in each command that needs it). Never write it to a file, a commit, a log or a decision record.
Needed: `repo` and `workflow` scopes (pushing `.github/workflows/*` needs `workflow`) and access to the organization; admin on a repository to enable Pages or change settings; a token for the GraphQL API (Discussions).
Before every commit: `git grep --cached -nE "ghp_[A-Za-z0-9]{10}|github_pat_" | wc -l` must print `0`. If a token has appeared in a transcript, ask the owner to rotate it.

Git over HTTPS without a stored credential (write it exactly like this in `sh`):

```sh
HDR="Authorization: Basic $(printf 'x-access-token:%s' "$GITHUB_TOKEN" | base64 -w0)"
git -c http.https://github.com/.extraheader="$HDR" push origin main
```

The database server needs the token too, and **at start**: `export GITHUB_TOKEN`, then `python tools/fi.py db up`. If `db push` says `could not read Username`, run `db down`, export the token, `db up`, push again.

## 2. Sandbox facts (learned the hard way)

- The shell is `sh` (dash), not bash: no arrays, no `set -o pipefail`, no `<(...)`. Use `bash script.sh` for bash. Never nest heredocs with the same terminator.
- One command may run at most 300 seconds. Run long jobs with `nohup ... &` and poll (`fi acquire` on a project with thousands of comments takes minutes).
- Background servers may disappear between turns; the data directory survives while the sandbox does. `fi db up` is idempotent: call it first. After a reset only git and GitHub remain: `fi db pull` restores the database.
- **One server serves one data directory, fixed when it starts.** A bare `fi db up` in another checkout (no `FI_HOME`), or the self-test, can leave a server running against a *different* database; `fi db up` then says "already running". Always export `FI_HOME` first, and check that `fi status` shows the database you expect before trusting any "no changes" result. `fi db up` now warns when the server was not started from this `FI_HOME`.
- `pkill -f` and `pgrep -f` match their own command line and kill your shell: use `pkill -x doltgres`.
- Never gate anything on a pipe: `cmd | tail` and `cmd | grep -q` hide the exit status or close the pipe early. Capture the output, check the status, then continue.

## 3. Restoring the environment

```sh
export GITHUB_TOKEN=...
git -c http.https://github.com/.extraheader="$HDR" clone https://github.com/open-commons-observatory/foss-insights.git
git -c http.https://github.com/.extraheader="$HDR" clone https://github.com/open-commons-observatory/<project>-fi.git
cd <project>-fi && git remote add template https://github.com/open-commons-observatory/foss-insights.git
pip install -r requirements.txt && tools/install-doltgres.sh /usr/local/bin
export FI_HOME=/tmp/<project>-fi-home      # data directory; any path outside the repository
python tools/fi.py db up && python tools/fi.py db pull && python tools/fi.py status
```

## 4. Procedures

**Analysis loop** (phases 5 and 6): `db pull`, `status`, `next -n 12`, `read ...`, write `batches/NNNN-*.tsv` at once, `apply --dry-run`, `apply`, `db push`. Twelve items per round; never read a second set before the first is written.

**Publishing an FI repository:** `render`, `export`, render twice and `diff -r` (deterministic), `check`, **`db push` (check its exit status)**, commit, push the repository, watch `Self-test` and `Publish site`, open the live URL and compare its numbers with `fi sql`. Push the database **before** the repository: pushing the database triggers no workflow, and CI clones it from GitHub and fails if the committed pages differ from a fresh render.

**Changing the template:** edit, run `bash tests/run.sh` three times (`env -u FI_TAXONOMY -u FI_DATABASE -u FI_MAINTAINERS FI_HOME=<fresh dir> timeout 200 bash tests/run.sh`), push only if all pass (use `if ...; then ...; fi`), then poll the workflows until complete and check the live site if pages changed. Record the decision (a new record) and any lesson in the same commit.

**Taking a template update into an FI repository:**

```sh
git fetch template
git checkout template/main -- AGENTS.md tools tests .github playbook docs/templates docs/queries docs/pages.yaml requirements.txt db
git diff --no-renames --diff-filter=D --name-only HEAD template/main -- tools tests .github playbook docs/templates docs/queries db | xargs -r git rm -q --
# add new facets from the template's taxonomy.yaml to yours (keep your own facets), then:
python tools/fi.py db init && python tools/fi.py render && python tools/fi.py export && bash tests/run.sh
```

`--no-renames` matters: git otherwise pairs a deleted file with an added one as a rename and the list of deletions comes back empty.

**Adding a migration:** a new `db/migrations/NNN-name.sql` (each statement ends with `;` at the end of a line), the new tables added to `TABLE_KEYS` in `tools/fi.py`, a test that upgrades an old-schema database with data, and a decision record.
**Adding a page:** SQL in `docs/queries/`, template in `docs/templates/`, an entry in `docs/pages.yaml`, navigation in `docs/templates/mkdocs.yml.j2`, and a test assertion with numbers calculated by hand.
**Verifying a claim about another project:** clone it, read the **lines** (not just file names), and record the commit and date you checked.
**Researching what a maintainer wrote:** fetch every comment of the repository through the API and search it yourself (do not rely on GitHub search: the key thread was missed by a keyword search once). Search comments, review comments, issue and PR descriptions, commit messages and Discussions.

## 5. Checks

**State check (start of a session):** the heads of `main` on GitHub against what `ROADMAP.md` and the last decision records say; the live pages return 200; `fi status` against the numbers the repository claims. Report any difference before working.
**Before you report "done":** CI green; live page opened; numbers compared with the database; anything important recomputed by a second path; secrets scan clean; `ROADMAP.md` and the records updated.

## 6. How to report

Three parts: **Done** (only what you ran and saw), **Not done** (including what you did not read and what is your judgement), **Next**. Own mistakes are stated plainly, with what was done about them.
