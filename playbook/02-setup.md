# 2. Setup

Create your FI repository: use this repository as a template (**Use this template**), name it `<project>-fi`, make it
public if you want GitHub Pages on a free plan. Then edit `fi.yaml`: `name`, `title`, `repo` (the FI repository itself),
`source.repo` (the project being analysed) and `source.maintainers`.

```bash
pip install -r requirements.txt
tools/install-doltgres.sh            # pinned Doltgres release into ~/.local/bin
export GITHUB_TOKEN=...              # from the environment only; never written to a file or committed
python tools/fi.py db init        # starts the server, creates the schema, loads taxonomy.yaml
```

Where things live:

- **The database** lives in `$FI_HOME/data` (default `~/.cache/foss-insights/<name>`), **outside the repository**.
  Doltgres writes `.doltcfg/` into its working directory; `fi` starts it from `$FI_HOME` so nothing leaks into git.
- **GitHub** holds the database in the hidden ref `refs/dolt/data` of the FI repository (`fi db push` / `fi db pull`).
  Ordinary `git clone` does not download it. The repository must already have one commit.
- **The token** needs read access to the analysed project's public data (a fine-grained token with no extra scopes is
  enough) plus write access to the FI repository for `db push`.

Servers do not persist in every environment (for example some sandboxes drop background processes between commands).
`fi db up` is idempotent: call it at the start of every session.

`tests/run.sh` and the self-test workflow check the tooling with their own fixture vocabulary (`tests/fixtures/`), so keep them in
your FI repository. If you customise the page templates, update the page names the test looks for.

**Credentials belong to the server process.** `db push` and `db pull` are executed by the database server, so `GITHUB_TOKEN` must be exported *when the
server starts*. If a push fails with `could not read Username`, the server was started without it: export the token, then `fi db down` and `fi db up`.
`fi db push` reports a failed push as an error; always check its exit status before pushing the repository, because CI clones the database from GitHub.
