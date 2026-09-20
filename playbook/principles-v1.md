> **Archived (v1, markdown records).** Kept for reference. The current method is in [README.md](README.md); see [migration-from-v1.md](migration-from-v1.md).

# Principles

These are the rules the first run followed (or paid for not following). Every procedure refers back to them.

1. **The records are the source of truth.** One markdown file per issue/PR/commit. `STATE.json` and `indexes/` are derived and can always be regenerated. Never hand-edit derived files.
2. **Atomic batches.** All manual tagging goes through a batch file applied by the tool. The whole batch is validated first; one bad tag rejects everything and nothing is written. Batches are archived, so the dataset can be rebuilt by replaying them.
3. **Controlled vocabulary with replace semantics.** A tag is `facet:value`; only values from the taxonomy are accepted. Mentioning a facet on a line *replaces* its previous values, so when you add one value to a multi-valued facet you must restate the others.
4. **Every claim says how it is known.** `conf:stated` (the maintainer said it), `reported` (a user said it), `inferred` (my reading). An inference is upgraded only when someone states it.
5. **Every record says how deeply it was read.** `depth` is `title`, `thread` (brief), `full` (whole thread) or `source` (checked against code/docs). Never let a count hide depth.
6. **Use the API, not HTML.** Complete, structured, rate-limited by a token. The scraped page of the first run held only ~15 comments per thread and cost a whole audit to repair. The token comes from an environment variable and is never stored, printed or committed.
7. **Compute coverage; never recall it.** Any number you state about what was read comes from a command run at that moment.
8. **State limits before results.** Truncated reads, skipped short replies, unexecuted claims, unread sources: written down next to the findings.
9. **Correct in the open.** A wrong record is fixed in the record, in every analysis document that repeated it, and in the log. Retractions stay visible.
10. **Summaries are your own words.** No copied passages; short paraphrase; non-technical speculation is left out or flagged unverified.
11. **Keep noise, tag it.** Spam, off-topic and support chatter are records with `kind:spam`; the noise ratio is itself a finding.
12. **Resumable rounds.** Read a bounded set, write its batch immediately, apply, validate, commit. Tool outputs can be cleared from context; the batch file is the memory.
13. **Opt-in procedures.** A goal decides what to do. Skipping a procedure is normal; not saying that you skipped it is the mistake.
