# input-remapper-oco-atlas

An [OCO Atlas](https://github.com/open-commons-observatory/oco-atlas) of [sezanzeb/input-remapper](https://github.com/sezanzeb/input-remapper):
an evidence-backed, versioned map of the problems reported against it, and a queue of pull requests that could close them.

**Read it:** https://open-commons-observatory.github.io/input-remapper-oco-atlas/ (the same pages are readable on GitHub in
[`docs/generated/`](docs/generated/index.md)). Start with [coverage](docs/generated/coverage.md): it says what has and has not been read,
with numbers computed from the database when the pages were rendered.

- **Lens:** contribution ([scope](SCOPE.md)). Goal: group the issues into recurring problems, triage them, and form PRs against the fork
  [`grenudi/input-remapper`](https://github.com/grenudi/input-remapper).
- **Data:** a Doltgres database in this repository's hidden ref `refs/dolt/data`; the readable form is [`data/`](data/) (CSV) and
  [`batches/`](batches/) (every batch of tagging, in order).
- **Method:** [`playbook/`](playbook/README.md).

## Continue the analysis

```bash
pip install -r requirements.txt && tools/install-doltgres.sh
export GITHUB_TOKEN=...                      # environment only
python tools/atlas.py db pull                # clone the database from this repo
python tools/atlas.py status                 # where things stand
python tools/atlas.py next -n 12             # what to read next
python tools/atlas.py read $(python tools/atlas.py next -n 12)
```

Then write `batches/00NN-*.tsv`, `atlas apply` it, `atlas db push`, `atlas render`, `atlas export`, commit and push
(see [phase 5](playbook/05-read-and-tag.md) and [phase 8](playbook/08-publish.md)).

## Lineage

Migrated from `input-remapper-prior-art` (markdown records) by replaying its batches; see [decisions/](decisions/).
