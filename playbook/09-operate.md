# 9. Operate across sessions

State lives in the database, not in a checkpoint file, so it cannot go stale:

```bash
python tools/fi.py db pull       # first thing in a new session or on a new machine (clones or updates)
python tools/fi.py status        # where things stand
python tools/fi.py next -n 12    # where to continue
```

- **Resume:** `db pull`, `status`, `next`. Nothing else is needed.
- **Refresh** an existing FI repository: `fi acquire` (idempotent), then read only what `next` returns, plus any items whose thread
  changed.
- **History and undo:** every batch is a database commit. `SELECT * FROM dolt_log`, `dolt_diff('HEAD~1','HEAD','tag')`, and
  `SELECT ... FROM tag AS OF 'HEAD~3'` show what changed and when; `SELECT dolt_reset('--hard', 'HEAD~1')` undoes a bad batch.
- **Rebuild from scratch:** re-apply the archived batches in order, `.tsv` and `.sql` alike (`fi db init`, `fi acquire`, then `fi apply` each file).
- **Autonomous rounds** (an agent working unattended): run rounds of 12; after each, `apply` + `db push`; stop on a scope question,
  a rate limit, or when context is running low. The last pushed commit is the resume point.
- **Ephemeral environments:** call `fi db up` first, `db pull` if the data directory is empty, and `db push` after every batch.

## Updating an FI repository from the template

An FI repository is created from the template with a clean history, so there is no automatic link back. To take template fixes:

```bash
git remote add template https://github.com/open-commons-observatory/foss-insights.git   # once
git fetch template
git checkout template/main -- tools tests .github playbook docs/templates docs/queries docs/pages.yaml requirements.txt db
python tools/fi.py render && python tools/fi.py export && bash tests/run.sh
git add -A && git commit -m "update tooling from template"
```

Files the template **deleted or renamed** are not removed by a checkout. List and remove them:

```bash
git diff --diff-filter=D --name-only HEAD template/main -- tools tests .github playbook docs/templates docs/queries db | xargs -r git rm -q --
```

This replaces the tooling and documentation and leaves your data and configuration alone (`fi.yaml`, `taxonomy.yaml`, `SCOPE.md`,
`batches/`, `decisions/`, `data/`, `docs/generated/`). If you customised a template or query, run `git diff template/main -- docs/templates`
first. A schema change would ship as a numbered migration in `db/migrations/` (none exists yet).
