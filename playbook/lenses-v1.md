> **Archived (v1, markdown records).** Kept for reference. The current method is in [README.md](README.md); see [migration-from-v1.md](migration-from-v1.md).

# Goal presets

Pick the closest preset, tick its procedures in your copy of [`templates/plan.md`](templates/plan.md), then adjust. `●` = do, `○` = optional, blank = skip.

| Procedure | G1 Quick landscape | G2 Exhaustive dataset | G3 Rule catalogue | G4 Successor comparison | G5 Design history | G6 Support/docs burden | G7 Detector / oracle input | G8 Refresh an existing analysis | G9 PR triage |
|---|---|---|---|---|---|---|---|------|
| P00 Goals and scope | ● | ● | ● | ● | ● | ● | ● | ●  ● |
| P01 Environment, credentials | ● | ● | ● | ● | ● | ● | ● | ●  ● |
| P02 Scaffold | ● | ● | ● | ● | ● | ● | ● |   ● |
| P03 Issues and PRs | ● | ● | ● | ● | ○ | ● | ● | ●  ● |
| P04 Commits | ○ | ● | ● | ● | ● |  | ○ | ●  ○ |
| P05 Taxonomy | ○ | ● | ● | ● | ● | ● | ● |   ● |
| P06 Bootstrap | ● | ● | ● | ● | ● | ● | ● | ●  ● |
| P07 Rule-tag commits | ○ | ● | ● | ● | ● |  | ○ | ●   |
| P08 Atomic batch loop | ○ | ● | ● | ● | ● | ● | ● | ●  ● |
| P09 Read issues at depth | ○ | ● | ● | ● | ○ | ● | ● | ●  ● |
| P10 Audit hidden text |  | ● | ● | ○ |  | ○ | ● |   ○ |
| P11 Triage commits |  | ● | ● | ● | ● |  | ○ | ●   |
| P12 Read commit diffs |  | ○ | ● | ○ | ● |  | ○ |    |
| P13 Verify against another version |  | ○ | ● | ● | ○ |  | ● |    |
| P14 Constraints catalogue |  | ○ | ● | ○ |  |  | ○ |    |
| P15 Analysis documents |  | ○ | ● | ● | ● | ○ | ● | ○  ○ |
| P16 Indexes and statistics | ● | ● | ● | ● | ● | ● | ● | ●  ● |
| P17 Second corpus |  | ○ |  | ● | ○ |  |  |    |
| P18 QA and corrections | ○ | ● | ● | ● | ● | ● | ● | ●  ● |
| P19 CI and publishing | ○ | ● | ● | ● | ● | ● | ● | ●  ● |
| P20 Backlog and log | ○ | ● | ● | ● | ● | ● | ● | ●  ● |
| P21 Rebuild and replay |  | ● | ● | ○ | ○ | ○ | ○ | ●  ○ |
| P22 Honest coverage reporting | ● | ● | ● | ● | ● | ● | ● | ●  ● |
| P23 Autonomous rounds |  | ● | ● | ○ | ○ | ○ | ○ |   ● |
| P24 Problem registry |  | ○ | ● | ○ | ○ | ● | ● |   ● |
| P25 Review the finished dataset | ○ | ● | ● | ● | ○ | ● | ● | ○  ● |

## What each goal is for

- **G1 Quick landscape** (hours). Titles plus opening posts, coarse kind/outcome tags, statistics. Answers "what goes wrong here, how often, who answers". Do not present it as exhaustive.
- **G2 Exhaustive dataset.** Every item tagged and summarised, depth recorded. The dataset is the deliverable; any report is generated from it.
- **G3 Rule catalogue.** G2 plus the `constraint` facet, full reads of every constraint-tagged thread, and verification against a newer version. Feeds validators and guards.
- **G4 Successor comparison.** Two corpora (project and successor/fork) with the same vocabulary; a status facet says which old finding still holds. See P13 and P17.
- **G5 Design history.** Commits in date order, decision-bearing commits and maintainer explanations; a timeline document. Diff reading matters more than issue reading.
- **G6 Support/docs burden.** Counts by kind, outcome, cause, per year; find docs gaps and repeated questions. Needs the taxonomy's `doc-gap` and `spam` values.
- **G7 Detector / oracle input.** For projects that measure or classify something: how failures are detected, where measurement misleads. Read for measurement validity, false positives and false negatives.
- **G8 Refresh.** New activity since the last run: re-list, bootstrap (idempotent), read only new items, regenerate indexes, add a session entry.

- **G9 PR triage.** G2 plus the `pr_potential` facet and a PR triage table as the deliverable. Each issue gets an actionability tag (code-fix, docs-fix, needs-design, upstream-dep, close-duplicate, wontfix). The output is a prioritised PR queue. Use when the end goal is contribution to the project, not just understanding it. Requires `conf:inferred` on `pr_potential`; upgrade to `conf:stated` when the maintainer confirms or rejects the approach.

## Combining goals

Presets compose: tick the union. The taxonomy (P05) is the one place where goals conflict, because each goal wants different facets. Decide facets from the union of goals *before* tagging; adding a facet later means re-reading records.
