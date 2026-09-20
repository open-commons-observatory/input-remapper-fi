# 5. Read and tag in rounds

One round = a bounded set (12 items works well), read, written down at once, applied, committed, pushed. Never read a second set
before the first batch is written: tool output can disappear from context; **the batch file and the database commit are the memory**.

```bash
python tools/atlas.py next -n 12
python tools/atlas.py read 90 91 93 94 95 98 99 100 101 102 103 104
```

`read` prints the opening post, maintainer replies (`M`) and user replies (`u`), and warns when the number of comments fetched
differs from what GitHub reports (the hidden-text check).

Write `batches/NNNN-<what>.tsv`, one line per item:

```
i93 | - | kind:bug conf:stated cause:environment pr_potential:upstream-dep depth=full | Two identical gamepads shown as one device; fixed by adding the physical path to the identity.
```

Fields: item, `-` (reserved), tags (`facet:value`, plus `depth=`), summary in your own words. Lines starting with `#` are comments.

```bash
python tools/atlas.py apply batches/0007-issues-90-104.tsv --dry-run   # validate only
python tools/atlas.py apply batches/0007-issues-90-104.tsv
python tools/atlas.py db push
```

`apply` checks **every** line first (item exists, facet and value are in the vocabulary, single-valued facets have one value,
summary present) and writes nothing if any line fails. A line is the full truth for its item: existing tags of that item are
replaced. The batch is one database transaction and one commit. Keep applied batch files in git: they are the readable audit log.

Summaries are your own words: no copied passages, no speculation about people. Record how each claim is known with `conf`:
`stated` (the maintainer said it), `reported` (a user said it), `inferred` (your reading).
