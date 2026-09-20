# Principles

The rules the first run followed (or paid for not following), revised for the database-backed method. Every phase refers back to them.

1. **The database is the source of truth.** Generated pages, CSV and indexes are derived: regenerate, never hand-edit.
2. **Atomic batches.** All manual tagging goes through a batch file applied by `atlas apply`. The whole batch is validated first;
   one bad line rejects everything and nothing is written. Applied batches are archived in git.
3. **A controlled vocabulary the database enforces.** A tag is `facet:value`; values outside `taxonomy.yaml` cannot be stored.
   A batch line is the full truth for its item: its previous tags are replaced.
4. **Every claim says how it is known.** `conf:stated` (the maintainer said it), `reported` (a user said it), `inferred` (your
   reading). An inference is upgraded only when someone states it.
5. **Every record says how deeply it was read.** `depth` is `title`, `thread`, `full` or `source`. Never let a count hide depth.
6. **Use the API, not HTML.** Complete, structured, rate-limited by a token. The token comes from the environment and is never
   stored, printed or committed.
7. **Compute coverage; never recall it.** Any number you state about what was read comes from a command run at that moment.
8. **State limits before results.** Truncated reads, skipped short replies, unread PRs, unverified claims: written next to the findings.
9. **Correct in the open.** A wrong record is fixed by a new batch line; the commit history keeps the correction visible.
10. **Summaries are your own words.** No copied passages; short paraphrase; speculation about people is left out.
11. **Keep noise, tag it.** Spam, off-topic and support chatter are items with `kind:spam`; the noise ratio is itself a finding.
12. **Resumable rounds.** Read a bounded set, write its batch immediately, apply, push. The database commit is the memory.
13. **Opt-in phases.** The lens decides what to do. Skipping a phase is normal; not saying so is the mistake.
14. **Same data, same bytes.** Rendering and export are deterministic and CI checks it, so a diff always means the data changed.
15. **Look things up; do not recall them.** Versions, limits, licences and maintenance status of every dependency are checked when
    you adopt it (two tools in this project's own stack were abandoned or pivoted while we chose them).
16. **A tool that says "valid" must be able to say "invalid".** Prefer constraints in the database over checkers that skip what they
    do not recognise.
