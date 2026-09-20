# ADR-0004: Upgrade to the register and project health; what the maintainer has said

Status: done (2026-09-20). Template decisions: ADR-0004 (methodology) and ADR-0005 (Discussions) in [foss-insights](https://github.com/open-commons-observatory/foss-insights).

**Upgrade.** The tooling was updated from the template and `fi db init` migrated this database in place (migrations 001 and 002). Checked before and after: 1,099 items, 192 analyses,
1,662 tags and the 21 evidence links of the five earlier problems were unchanged; the five became register entries. `fi acquire` then added 5,306 comments (author, item and date only), 30 releases and 221 discussions.
Also acquired: one item that appeared after the earlier fetch (now 1,100 items: 840 issues, 260 pull requests).

**Health figures were recomputed independently** (plain Python over a raw dump, no SQL) and match the rendered page exactly: comments per year by maintainers and others, median days to first response,
share of issues never answered, discussions without a reply. "Maintainers" here are the two configured logins (sezanzeb, jonasBoss), so these counts are larger than the maintainer's own.

**What the maintainer has written** was collected from every channel (comments, review comments, issue and PR descriptions, commit messages, Discussions) and read where it matched; the central thread is #853 "State of Maintenance",
with the 2026-03-22 replies. It produced six register entries (batch 0019): a risk (maintainer stepped back), an improvement in progress (dependency injection for testability), an improvement (architecture hard to approach),
a request (Qt interface), an improvement (backlog not triaged) and a known error (arbitrary characters cannot be injected). Batch 0020 gave the five earlier entries value, effort, risk and change type.

**Limits stated at the time.** Not every comment was read line by line. The health metrics cannot tell a busy maintainer from a departed one; the register says so and rests the risk on his own statements.
Value, effort and risk are analyst judgement (`conf:inferred` where not stated by a maintainer). The 260 pull requests remain unanalysed; 52 actionable items are in no register entry; 19 `pr_potential:unknown` items need a second look.

**Corrected:** `SCOPE.md` had listed Discussions as out of scope as "too sparse"; it is now in scope (metadata).
