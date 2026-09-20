# 5. Read and tag in rounds

One round = a bounded set (12 items works well), read, written down at once, applied, committed, pushed. Never read a second set
before the first batch is written: tool output can disappear from context; **the batch file and the database commit are the memory**.

```bash
python tools/fi.py next -n 12
python tools/fi.py read 90 91 93 94 95 98 99 100 101 102 103 104
```

`read` prints the opening post, maintainer replies (`M`) and user replies (`u`), and warns when the number of comments fetched
differs from what GitHub reports (the hidden-text check).

Write `batches/NNNN-<what>.tsv`, one line per item:

```
i93 | - | kind:bug conf:stated cause:environment pr_potential:upstream-dep depth=full | Two identical gamepads shown as one device; fixed by adding the physical path to the identity.
```

Fields: item, `-` (reserved), tags (`facet:value`, plus `depth=`), summary in your own words. Lines starting with `#` are comments.

```bash
python tools/fi.py apply batches/0007-issues-90-104.tsv --dry-run   # validate only
python tools/fi.py apply batches/0007-issues-90-104.tsv
python tools/fi.py db push
```

`apply` checks **every** line first (item exists, facet and value are in the vocabulary, single-valued facets have one value,
summary present) and writes nothing if any line fails. A line is the full truth for its item: existing tags of that item are
replaced. The batch is one database transaction and one commit. Keep applied batch files in git: they are the readable audit log.

Summaries are your own words: no copied passages, no speculation about people. Record how each claim is known with `conf`:
`stated` (the maintainer said it), `reported` (a user said it), `inferred` (your reading).

## Bulk edits: `.sql` batches

A re-tag that touches many items (for example a vocabulary change) is a `batches/NNNN-<what>.sql` file: plain `UPDATE`/`INSERT` statements, each ending
with `;` at the end of a line. `fi apply` runs the whole file in **one transaction** (the database's constraints are the validator) and commits
it as one commit; a failing statement leaves everything untouched. Use explicit item numbers, not sub-selects, so replaying the file later gives the
same result. Keep the evidence for the rule in a comment at the top of the file.
