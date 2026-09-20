# 2. Setup

Create your atlas: use this repository as a template (**Use this template**), name it `<project>-oco-atlas`, make it
public if you want GitHub Pages on a free plan. Then edit `atlas.yaml`: `name`, `title`, `repo` (the atlas repo itself),
`source.repo` (the project being analysed) and `source.maintainers`.

```bash
pip install -r requirements.txt
tools/install-doltgres.sh            # pinned Doltgres release into ~/.local/bin
export GITHUB_TOKEN=...              # from the environment only; never written to a file or committed
python tools/atlas.py db init        # starts the server, creates the schema, loads taxonomy.yaml
```

Where things live:

- **The database** lives in `$ATLAS_HOME/data` (default `~/.cache/oco-atlas/<name>`), **outside the repository**.
  Doltgres writes `.doltcfg/` into its working directory; `atlas` starts it from `$ATLAS_HOME` so nothing leaks into git.
- **GitHub** holds the database in the hidden ref `refs/dolt/data` of the atlas repo (`atlas db push` / `atlas db pull`).
  Ordinary `git clone` does not download it. The repository must already have one commit.
- **The token** needs read access to the analysed project's public data (a fine-grained token with no extra scopes is
  enough) plus write access to the atlas repo for `db push`.

Servers do not persist in every environment (for example some sandboxes drop background processes between commands).
`atlas db up` is idempotent: call it at the start of every session.

`tests/run.sh` and the self-test workflow check the tooling with their own fixture vocabulary (`tests/fixtures/`), so keep them in
your atlas. If you customise the page templates, update the page names the test looks for.
