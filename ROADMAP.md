# Roadmap of this analysis (input-remapper)

Kept up to date by whoever works here (see `AGENTS.md`). Numbers go stale: run `python tools/fi.py status` and read `docs/generated/coverage.md`. Reasons are in `decisions/`; the template's own plan is in the template repository.

## State at 2026-09-20 (verify with `fi status`)
Register of 11 entries (see `docs/generated/register.md`); health measured (`health.md`); 192 of 840 issues analysed (through #283), none of the 260 pull requests; 52 actionable items are in no register entry; 19 `pr_potential:unknown`.

## Next, in order
1. **Read the 260 pull requests** (`fi next --kind pr`, rounds of 12). Link merged fixes to issues; this prunes the register and shows how the maintainer reviews.
2. **Assign the 52 unassigned actionable items** to register entries, verifying each against the current upstream source first (record the commit); take a second look at the 19 `unknown`.
3. **Verify what could not be checked without a running interface:** the "Restore Defaults" flow (redesigned upstream), #94 autoload discoverability, #270 BTN_BACK naming.
4. **Read the text of the most relevant Discussions** (only their metadata is stored).
5. **Continue the issues from #284**, twelve at a time.

## Contribution drafts (the owner's fork `grenudi/input-remapper`)
Branches and diffs only; **no pull request upstream without the owner's say**. Order of evidence: (1) a `modules-load.d` entry for `uinput` plus a README troubleshooting note; (2) an FAQ entry stating the Wayland per-application limit and the workaround; (3) contributed OpenRC and runit scripts (needs testers; the maintainer asked for a PR in #15); (4) continuing dependency injection in small steps: first read PRs #960, #964, #1003 and #1068 to match his review style, then ask him. His rules: unit tests, pylint, black.

## Open questions for the owner
Whether to open the documentation pull requests upstream once drafted; whether to offer help with issue triage to the maintainer.
