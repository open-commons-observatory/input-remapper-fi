# 9. Operate across sessions

State lives in the database, not in a checkpoint file, so it cannot go stale:

```bash
python tools/atlas.py db pull       # first thing in a new session or on a new machine (clones or updates)
python tools/atlas.py status        # where things stand
python tools/atlas.py next -n 12    # where to continue
```

- **Resume:** `db pull`, `status`, `next`. Nothing else is needed.
- **Refresh** an existing atlas: `atlas acquire` (idempotent), then read only what `next` returns, plus any items whose thread
  changed.
- **History and undo:** every batch is a database commit. `SELECT * FROM dolt_log`, `dolt_diff('HEAD~1','HEAD','tag')`, and
  `SELECT ... FROM tag AS OF 'HEAD~3'` show what changed and when; `SELECT dolt_reset('--hard', 'HEAD~1')` undoes a bad batch.
- **Rebuild from scratch:** re-apply the archived batches in order (`atlas db init`, `atlas acquire`, `atlas apply` each file).
- **Autonomous rounds** (an agent working unattended): run rounds of 12; after each, `apply` + `db push`; stop on a scope question,
  a rate limit, or when context is running low. The last pushed commit is the resume point.
- **Ephemeral environments:** call `atlas db up` first, `db pull` if the data directory is empty, and `db push` after every batch.
