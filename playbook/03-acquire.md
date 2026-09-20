# 3. Acquire

```bash
python tools/fi.py acquire            # issues + PRs + commits of source.repo
python tools/fi.py acquire --items-only
```

By default it also collects activity: every issue and code-review comment (who, where, when; never the text), releases, and **GitHub Discussions** (GraphQL, needs a token).
That feeds the [health](10-project-health.md) page. `--activity-only` refreshes just that part.

Uses the GitHub REST API (never scraped HTML: a scraped page holds only part of a long thread). It is idempotent: re-running
refreshes existing rows and adds new ones (this is the whole "refresh" procedure). Issues and PRs share one number space, so
both live in `item` (`is_pr`, `state` = OPEN / CLOSED / MERGED). Commits land in `git_commit`.

Check the count against the GitHub UI or `open_issues_count` before trusting it, and record what was **not** acquired (wiki, external forums, the text of Discussions) in `SCOPE.md`, with the number that justifies leaving it out. Unauthenticated calls are limited to 60/hour; use a token.

To load a saved API response instead of calling GitHub (offline work, tests): `--items-json FILE --commits-json FILE`.
