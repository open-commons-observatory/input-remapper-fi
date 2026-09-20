> **Archived (v1, markdown records).** Kept for reference. The current method is in [README.md](README.md); see [migration-from-v1.md](migration-from-v1.md).

# Maturity: what has been tested, how, and what has not

This playbook is **a documented method with a working reference implementation, proven on one large project and smoke-tested on a second. It is not battle-tested.** Everything here was derived from a single analysis (zapret and zapret2, 3,249 records) by a single operator. Nobody else has used it. Treat it as a strong first draft to be corrected by the next real use, and fix it in the same session when reality disagrees (pitfall 40).

## Evidence, by level
| Level | What it means | What has it |
|---|---|---|
| **Used at scale** | run for real on the first project, hundreds of batches | P01-P11, P13-P23 (fetching, bootstrap, batches, reading at depth, audit, triage, rules, documents, indexes, second corpus, QA, CI, log, rebuild proof twice, coverage reporting, autonomous rounds) |
| **Used lightly** | exercised, but on a small selection or once | P12 diffs (82 commits of about 2,300), P24 registry (one project), P25 review (one project plus the trial), `stamp` |
| **Written, not exercised** | described from reasoning only | P00 as a formal step (the first run's scope was informal), goal presets G4-G8 as presets (the run followed G2/G3 with G4 elements) |

## Second project trial (an unrelated Rust CLI: 897 issues and PRs, 1,018 commits)
Ran fetch, bootstrap, rule-based tagging, strict apply, review, stamp and a from-scratch replay: **zero differing records**. It found four real defects that the first project never showed, all fixed and now covered by tests: generic tools recorded title-only tagging at depth `thread`; the review flagged shares computed on three records; PRs (69% of that tracker) need the merge state to derive outcomes; the review needed the maintainer login when no `project.json` was present. It did **not** exercise deep reading, the registry or the rule catalogue on that project.

## Automated tests
`reference-implementation/tests/test_reference.py` (offline, no token; runs in CI): 16 checks over a synthetic repository: bootstrap counts, validate, rule generation with depth and PR state, strict apply with atomic rejection, append idempotence, inferred classes, stamp, review, registry generation, and a byte-for-byte replay. It was mutation-tested: two deliberate breakages were both caught. **Not covered by tests:** the network paths (`threads.py`), `import-docs`, the bootstrap heuristics, Windows, and any scale beyond a handful of records.

## Measured scale
On 3,249 records (13 MB, one file per record): `pz.py status` 1.1 s, `validate` 0.2 s, `index` 0.6 s, `review.py` 0.5 s, `registry.py generate` 0.3 s; the full rebuild from batches about one minute. Every command parses every record, so cost is roughly linear; **nothing above about 3,000 records has been tried.**

## Known gaps (not tested, not designed for)
- **Other trackers** (GitLab, Jira, Bugzilla, mailing lists, forums): only the GitHub REST API is implemented; GraphQL Discussions are not fetched.
- **Very large projects** (tens of thousands of issues): file-per-record and parse-everything will need work; API rate limits need a longer fetch plan.
- **More than two corpora**: needs code changes (`REPOS`, `rec_dir`); the ids `z1`/`z2` are labels from the first project.
- **Several maintainers or a community-answered tracker**: the review and `maintainers` logic assumes a small list of logins; not tried with many.
- **Non-Latin and mixed-language trackers**: the first project was Russian and English; keyword rules (symptoms, heuristics) are English-centric and precision on other languages is unknown.
- **Windows shells and other Python versions**: developed and tested on Linux with a recent Python 3 only.
- **Keyword heuristics** (`--heuristics zapret`, symptom rules) are project-specific examples with measured precision of about two thirds; they must be rewritten and re-measured for a new project.
- **No versioning, changelog or licence yet**; the repository is private.
- **Single-source knowledge in the example dataset**: findings in the first project rest on one maintainer's statements plus code, untested by experiment (see its review).


## Third project trial (input-remapper: ~1 370 issues and PRs; started 2026-09-20)
New project shape: a Linux input-device remapping tool (Python + GTK + evdev), public tracker, one primary maintainer, English-language issues, active since 2020. Goal is contribution (G2 + G6 + G9 PR triage), not just analysis. Differences from the first two runs that this trial is designed to stress-test: (a) the `pr_potential` facet (new; designed at P00); (b) G9 goal preset (new; forks share the upstream issue tracker, so no z2 from the issue side); (c) single-maintainer dominance (~84% of commits) as a confidence-mix signal. This entry will be updated as the run progresses and findings are recorded.

## What would raise the level
Run it on a third project with a different shape (many maintainers, or a non-GitHub tracker), by someone else if possible, and record every friction in `lessons/pitfalls.md`; run the deep-reading loop, the registry and the rule catalogue on the trial project; add a scale test at 20,000+ records; add versioning and a changelog.
