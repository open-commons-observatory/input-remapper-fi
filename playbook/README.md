# The method

An atlas is built in nine phases. Each phase is one short document and, mostly, one `atlas` command.
Skipping a phase is normal; not saying that you skipped it is the mistake ([principle 13](principles.md)).

| # | Phase | Command | Document |
|---|---|---|---|
| 1 | Decide what the atlas is for | (edit `atlas.yaml`) | [scope and lens](01-scope-and-lens.md) |
| 2 | Set up the environment | `tools/install-doltgres.sh`, `atlas db init` | [setup](02-setup.md) |
| 3 | Acquire the corpus | `atlas acquire` | [acquire](03-acquire.md) |
| 4 | Design the vocabulary | (edit `taxonomy.yaml`) | [vocabulary](04-vocabulary.md) |
| 5 | Read and tag in rounds | `atlas next`, `atlas read`, `atlas apply` | [read and tag](05-read-and-tag.md) |
| 6 | Keep it honest | `atlas status`, `atlas check` | [quality and honesty](06-quality-and-honesty.md) |
| 7 | Group into problems and PRs | `atlas sql` | [problems and PRs](07-problems-and-prs.md) |
| 8 | Publish | `atlas render`, `atlas export`, `atlas db push` | [publish](08-publish.md) |
| 9 | Operate across sessions | `atlas db pull`, `atlas status` | [operate](09-operate.md) |

Also: [principles](principles.md) (13 rules), [lenses](lenses.md) (goal presets), [lessons](lessons.md) (what went wrong
while building this), [migration from v1](migration-from-v1.md). The archived v1 documents are `*-v1.md`.

## The loop in five lines

```bash
python tools/atlas.py next -n 12            # which unread items are next (the database is the cursor)
python tools/atlas.py read 90 91 93 ...     # read them through the API
$EDITOR batches/0007.tsv                    # one line per item: tags + summary
python tools/atlas.py apply batches/0007.tsv   # validate all, write atomically, commit
python tools/atlas.py db push               # the batch and its commit are now safe in GitHub
```
