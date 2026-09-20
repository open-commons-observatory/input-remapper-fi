# ADR-0001: Migrating input-remapper-prior-art into an OCO Atlas

Status: done (2026-09-20).

**What:** the v1 analysis repo `open-commons-observatory/input-remapper-prior-art` (one markdown file per record, `pz.py`) was
re-created as an atlas: same corpus, same vocabulary, same tagging, new storage.

**How:** created from the `oco-atlas` template; `taxonomy.yaml` converted from the v1 JSON (12 facets, 116 values);
`atlas acquire` re-fetched the corpus from the GitHub API; the 16 v1 batch files were replayed with `atlas apply` (batch format is
unchanged). The 259 pull requests and the 929 commits are acquired but not analysed, exactly as in v1.

**Verified (against numbers computed independently from the v1 batch files in DuckDB before migrating):** 1,099 items (840 issues,
259 PRs), 929 commits, 192 analyses, 1,662 tags, and an identical `pr_potential` distribution (89 unknown, 46 docs-fix, 20 code-fix,
18 needs-design, 13 upstream-dep, 6 wontfix).

**One repair, made in the open:** two v1 batch lines (#243, #246, batch 0015) had `conf=stated` / `conf=inferred` instead of
`conf:stated` / `conf:inferred`; v1's validator ignored them, so those two records had silently lost their confidence tag. The batch
file was corrected and the tags now exist. The v1 repo is unchanged.

**Not migrated:** v1 session notes (`brainstorms/`), `CHECKPOINT.json` (the database is the cursor now), the 929 v1 commit stub files
(re-acquired), v1 tools.
