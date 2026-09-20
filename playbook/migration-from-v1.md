# Migration from v1 (markdown records) to v2 (database)

v1 stored one markdown file per issue/PR/commit and used a Python reference implementation (`pz.py`). It is preserved at tag
`v1-markdown-records` and in git history. The tagging method carries over; the storage and the mechanical procedures do not.

| v1 procedure | In v2 |
|---|---|
| P00 goals and scope | [phase 1](01-scope-and-lens.md); goal presets became [lenses](lenses.md) |
| P01 environment, credentials | [phase 2](02-setup.md) |
| P02 scaffold the repository | this template (**Use this template**) |
| P03 acquire issues and PRs | `atlas acquire` |
| P04 acquire commits | `atlas acquire` (commits stored; analysing them is [planned]) |
| P05 taxonomy | [phase 4](04-vocabulary.md); `taxonomy.yaml`, enforced by foreign keys |
| P06 bootstrap the records | gone: `acquire` creates the rows, `atlas next` is the cursor |
| P07 rule-tag commits, P11 triage commits, P12 read diffs | [planned] (commit analysis) |
| P08 atomic batch loop | `atlas apply` (same batch format) |
| P09 read issues at depth | `atlas read` |
| P10 audit hidden text | built into `atlas read` (comment-count check) |
| P13 verify against another version | manual, `depth=source` ([phase 7](07-problems-and-prs.md)) |
| P14 constraints catalogue | [planned] (rule-catalogue lens) |
| P15 analysis documents | generated pages plus hand-written documents in your atlas repo |
| P16 indexes and statistics | SQL queries and templates; `atlas render` |
| P17 second corpus | [planned] (schema is single-corpus) |
| P18 QA and corrections | [phase 6](06-quality-and-honesty.md) |
| P19 CI and publishing | [phase 8](08-publish.md); two workflows |
| P20 backlog and session log | the database commit log; `decisions/` for decisions |
| P21 rebuild and replay | re-apply archived batches, or `dolt_log` / `AS OF` |
| P22 honest coverage reporting | `atlas status`; the coverage page |
| P23 autonomous rounds | [phase 9](09-operate.md); the database is the checkpoint |
| P24 problem registry | `problem` and `problem_item` tables |
| P25 review the finished dataset | [phase 6](06-quality-and-honesty.md) |

**Batch files are compatible.** A v1 batch line (`i93 | - | kind:bug ... depth=full | summary`) applies unchanged with `atlas apply`.
That makes migration a replay: `atlas db init`, `atlas acquire`, then `atlas apply` each old batch in order.
