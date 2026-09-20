# 6. Quality and honesty

```bash
python tools/atlas.py status     # coverage, computed now
python tools/atlas.py check      # warnings; add --strict to fail CI on any
```

- **Coverage is computed, never recalled.** Any number you state about what was read comes from `status` or the coverage page at
  that moment. Issues and PRs are reported separately: reading only issues is fine, calling that "analysed 192 of 1099" is not.
- **State limits before results:** truncated reads, skipped short replies, unread PRs, unverified claims.
- **Watch the `unknown` share.** A dataset that is 46% `unknown` on the facet you care about is a to-do list, not a finding.
- **Correct in the open.** Fix the row (a new batch line), let the commit history show it, and note the correction in the log.
- **Trust constraints, not validators that skip things.** The database refuses bad tags; a hand-written checker that "passes"
  because it ignored a malformed token did exactly that once (see [lessons](lessons.md)).
- **Determinism:** `atlas render` and `atlas export` produce byte-identical output for the same database commit; CI enforces it.

Before publishing a summary, run a review pass: sample a few items and re-read them against their thread, check the top
counts by hand, and confirm every generalisation names the items behind it.
