> **Archived (v1, markdown records).** Kept for reference. The current method is in [README.md](README.md); see [migration-from-v1.md](migration-from-v1.md).

# Pitfalls (numbered; each cost real time in the first run)

Format: **symptom** - cause - fix - where it is handled.

## Data acquisition
1. **A third of the maintainer text was missing from constraint threads** - the issue list and thread cache had been scraped from HTML, which returns only the first ~15 comments - use the REST API (complete, paged) from the start - P03, P10.
2. **Maintainers who joined late were invisible** (three threads had zero maintainer replies in the cache, one with 263 comments) - first page only - compare `ncomments` from the API with the cached count - P10.
3. **The brief reader hid text** (first 160 characters of the post, first two maintainer replies cut at 200) - a reading window chosen for speed - measure the hidden text per issue and read it (audit) - P10.
4. **A reply cap silently discards content** - caps are lossy - measure what a cap loses before choosing it (1,000 characters kept 94%, 600 kept 87%) and state the cap - P09, P22.
5. **The command died after 300 seconds** - one shell command has a time limit - fetch in chunks of ~150 threads, cache per thread, use `timeout 240` - P01, P03.
6. **The public clone's history began late** - the project's public history was truncated - check the first commit date against the project's creation; state the range - P04.
7. **Discussions and forum threads were never read** - not in the REST issues API and not in scope - decide in P00, list as a limit - P00, P22.
8. **Numbering gaps and PRs sharing numbers** - deleted items, PRs and issues share one sequence - normal; keep PRs as records - P03, P17.

## Tool use and shell
9. **Directory literally named `{a,b}`** - `/bin/sh` does no brace expansion - write explicit `mkdir -p` lines - P01.
10. **A rejected batch still produced a commit whose message claimed the changes** - `pz.py apply ... | tail` returns `tail`'s exit status, so the failure was invisible - run `apply` alone, or `set -o pipefail`, and read the output - P08, P18.
11. **Session-entry script crashed after partial work** - the title contained `830/830` and `/` is a path separator - sanitise titles, write the file first, then append README and log, then verify - P20.
12. **Invalid UTF-8 in tool output** - `cut -c1-N` split a multi-byte character - cap text inside Python - P01.
13. **`time` not found** - the shell has no such builtin - measure with `date +%s` or Python - P01.
14. **A token appeared in a conversation** - pasted by the owner - never store or repeat it, read it from the environment, scan the repo before every push, advise rotation - P01, P19.
15. **Tool outputs disappeared from context** - long sessions clear old tool results - write the batch for what you just read *before* reading more - P08, P23.

## Batches and records
16. **Stray letters in refs** (`i1127b`, `i643b`, `i770b`, `i1260b`) - typed by hand - the atomic rejection caught them; use `pz.py check` before `apply` - P08.
17. **An analysed record's summary was overwritten** - a new line re-tagged an already analysed record without `+` - `check` warns; use `+ text` to append - P08, P18.
18. **A multi-valued facet lost values** - replace semantics: mentioning `cause:` replaced all causes - restate every value that still holds; `check` warns - P05, P08.
19. **`unknown class D9`** - the class did not exist - define classes early or use `-`; the atomic rejection protects the data - P05, P08.
20. **Records tagged by a title heuristic looked "done"** - `triaged` is not `analyzed` - only manual tags count in statistics - P06.
21. **Depth was defined late** (`full` and `source` added mid-way) - the first depth ladder had only `title/thread/source` - define the ladder before tagging - P05, P09.
22. **A successor-status facet added late** meant re-reading 82 records - the goal changed mid-run - decide in P00 whether a comparison will happen - P00, P13.
23. **Heuristic keyword rules did not transfer** - they encode one project's vocabulary - default `--heuristics none` in a new project - P06.
24. **Rules by subject text were unsafe** - subjects lie - only automate rules stated in one sentence and sample the matches - P07.

## Interpretation
25. **Wrong causal stories from brief reads** (one packet-counter explanation, one queue-ordering claim) - the full thread contradicted them - the correction protocol: record, every document, log - P18.
26. **Inference stated as fact** - a link inferred from commit timing - keep `conf:inferred` until the maintainer says it; then upgrade and say so - P09, P18.
27. **"Not found" reported as "does not exist"** - grep negatives are weak - write "found no X (searched A, B)" - P13.
28. **Claims about another version from its manual alone** - the manual may lag the source - check the source and name the function - P13.
29. **Nothing was executed** - conclusions from reading only - state it in every summary of results - P13, P22.
30. **Speculation recorded as evidence** (motives, budgets, politics) - it appears in long threads - leave it out or flag it unverified - P09.
31. **A rule without its mechanism** - copied from a thread without the reason - record the maintainer's stated mechanism - P14.

## Reporting and operations
32. **Numbers quoted from memory** ("about 160 remain"; the computed figure was 209) - compute from `pz.py status` or a script - P22.
33. **Backlog filed in the wrong repositories twice** - an org-wide notes folder, then another project's folder - keep the backlog in the analysis repo - P20.
34. **Similar project names were conflated** (a CLI library and the tool that uses it) - keep boundaries in the scope document and ask when unsure - P00.
35. **Rounds too big lost detail; rounds too small wasted calls** - 12 threads per round (full) and 36-40 items (brief) worked - P08, P23.
36. **Corrections left stale claims in documents** - a record was corrected but analysis documents still cited it - `grep -rn "#N" analysis/` on every correction - P18.
37. **Derived files were stale at push** - `index`/`status --write` not rerun - run them before the closing commit - P16, P19.

## Second run additions
41. **Typos in hand-typed refs, again and again** (`dc0fe0f`, `fd1cfd1`, `d06e4f4d`, `cb85262a`) - copying 7-character hashes from a listing by eye - generate batches from subject-pattern rules (`rulegen.py`) instead of typing hashes - P11.
42. **A rejected batch committed anyway, a second time** - `apply | tail` again masked the exit status although the lesson was already written down - never pipe `apply`; chain `check && apply && validate && commit` and read the result - P08.
43. **A statistic in a document was wrong by mental arithmetic** ("1,214 of 1,330, 91%"; the data said 1,132, 85%) - I summed months in my head - compute every figure in a document with a script and write the document from its output - P22.
44. **A method note misdescribed which batches used rules** - written from memory of the session - derive method statements from the batch headers and file names - P15, P22.
45. **A claim was narrower than my summary** - "keeps the last good list" was true only for files that cannot be opened (the code comment says why) - read the diff before summarising a code behaviour, and say "diff read" - P12.
46. **Reading budget is finite; say what was cut** - display caps and skipped short replies were used throughout the second corpus - state them in the session entry - P22.

## Registry run additions
47. **Regenerating documents would have broken the rebuild** - the class links of 1,170 records existed only as a side effect of parsing the old documents (`backfill-docs`) - freeze them as data in a batch first, then change documents - P24.
48. **The generator dropped a content block and only the rebuild diff caught it** (160 records lost their `cited_in`: the document views omitted the first-pass evidence notes) - a word-multiset comparison of each migrated entry plus a full rebuild proof after any structural change - P21, P24.
49. **Weak labels start noisy** - the first symptom rules matched "hang" inside "change", "reboot" inside "after reboot", a passing mention of Discord voice: about 60-65% precision on a 28-record sample - sample before applying, tighten, write the estimate in the batch header - P24.
50. **Leave-one-out accuracy was optimistic** (81-89%) because the training set was the problem-rich subset the documents had cited; a manual spot check on the second corpus gave about 70% - always spot-check on the population you will apply it to - P24.
51. **Machine suggestions must never look like evidence** - inferred classes live in `classes_inferred` and are shown apart from hand-cited ones - P24.
52. **An apostrophe in a single-quoted Python string broke a tool and the copy in the playbook** - a text edit made inside a script - run `py_compile` or the tool itself right after every edit, before copying or committing - P08.
53. **A per-record `auto` facet stayed at 30 records** - "could this be caught automatically" is a property of a proposed detector, not of an issue - keep it on the registry entry (computed from its proposals), not on records - P24.

## Review run additions
54. **A turn ended with only a backlog write, no answer in chat** - after filing the synthesis I stopped at the tool result and the owner had to ask again - finish every turn with the answer itself; the backlog entry is a record, not the reply - P20, P23.
55. **Hand-typed counts in READMEs and documents went stale four times** (770/60 vs 766/64 issues, 59 vs 61 diffs, a stale "734 title-only" paragraph, a wrong monthly sum) - write derived numbers only with `pz.py stamp` or a script - P16, P22.
56. **References in the rule catalogue were typed from memory** and five successor commits lacked their prefix - verify every `#N`, `z2#N` and hash programmatically before committing - P14.
57. **75% of records share their summary opening with another record** - group-tagged batch lines are efficient but make summaries group-level evidence; say so, and write unique text where the item adds information - P08, P25.
58. **The review found what a spot check would not** (documents citing a quarter of the records, all title-only tags stale, single-maintainer dependence, 29% unanswered threads) - run `review.py` when the main reading is done, not only at the very end - P25.

## Second-project trial additions
59. **Generic tools overstated the depth** - `apply` defaults issues to depth `thread`, so title-only rule batches looked like brief reads; invisible in the first project where depth was set by hand - rule and text tools now emit an explicit `depth=` (default `title`) - P08, P11.
60. **The review flagged shares computed on three records** - "67% unresolved" from three tagged issues - reports need a minimum sample size before flagging (30) - P25.
61. **PR-heavy trackers need the merge state** - 69% of the trial project's records were PRs whose outcome lives in `state`, not in the title - `rulegen --with-state` matches rules against the title plus `[state]` - P06, P09.
62. **A first-time-green test suite proves little** - mutation-test it: break two behaviours on purpose in a scratch copy and confirm the tests fail - P19.
63. **Readiness claims need evidence** - the playbook was described as finished before any second project had run it - state maturity from what was tested (`MATURITY.md`), and update it when that changes - P22.

## Meta
38. **"Complete" without a depth** - a count of analysed records hid that many were read shallowly - always give depth counts and limits together - P22.
39. **Scope expanded silently** (a second corpus) - fine when asked for, but record the decision in the entry - P17, P20.
40. **The playbook itself:** if a procedure here disagrees with what works, fix the playbook in the same session and add the lesson here.

## Input-remapper / PR triage additions

64. **A contribution goal needs its own actionability facet from the start** — the owner wanted PRs from the analysis, not just a dataset; the `pr_potential` facet had to be designed before the reading loop, not retrofitted mid-run. A retrofitted facet means re-reading every record that has already been tagged. Decide at P00 whether the goal is understanding or contribution; if contribution, add a `pr_potential`-style facet (values: code-fix, docs-fix, needs-design, upstream-dep, close-duplicate, wontfix, unknown) to the taxonomy before P06 — P05, P09, P24.

65. **Forks share the upstream issue tracker** — a GitHub fork does not create its own issue list. The fork is the contribution vehicle (where PRs land), not a second corpus. Do not treat it as z2 unless its commit history diverges meaningfully and you need G4 comparison — P00, P02, P17.

66. **A single-maintainer project's stated findings are single-source** — when one person wrote 80%+ of the commits and answered most issues, every `conf:stated` tag rests on one expert's view. Flag this in the ATTENTION section of `review.py` and in the P22 limits statement; it is not a reason to avoid using the data, but every claim should say who said it — P22, P25.
