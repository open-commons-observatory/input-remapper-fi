# ADR-0002: First triage pass and problem registry

Status: done (2026-09-20). Batches `0017` and `0018`.

**Finding 1: "unknown" hid two meanings.** 89 of 192 `pr_potential` tags were `unknown` (46%). Cross-tabulating them showed 70 sit on CLOSED items whose outcome is
`fixed` (61) or `workaround` (9): there "unknown" meant "already resolved", and the vocabulary had no value for that. **Decision:** add `pr_potential:resolved`
("closed with a fix, answer or workaround; no change to the project is needed") and re-tag those 70 by an explicit-ID `.sql` batch (0017). **Considered and rejected:**
re-tagging the other 19 from one-line summaries (would manufacture certainty). They stay `unknown` as the honest second-look list; three of them (#198, #220, #258)
are tagged `fixed` but are still OPEN upstream. Result: 19 unknown (10%), `atlas check` clean.

**Finding 2: several 2021 docs asks are already met upstream.** Checked against upstream `sezanzeb/input-remapper` at `cb8f5fd` (2026-09-14) by reading the docs and code,
not by file-name matches: #66 fixed in code, #11/#81 uninstall documented, #269 `python3-devel` documented. Re-tagged `resolved` (0018).

**Registry (0018), five problems, all `conf:inferred` until a maintainer confirms:** `uinput-module-not-loaded` (3 items), `no-non-systemd-init-scripts` (2),
`per-app-switching-wayland` (7), `requested-features-still-missing` (5), `already-fixed-or-documented-upstream` (4, closed).
Verified absent upstream: any `modprobe`/`modules-load.d` for uinput; any OpenRC/runit/sysv files; any statement of the Wayland focus limit; `text()` and LED macros,
udev classification, mapping search, notifications.

**Not done, on purpose:** 52 actionable items are not yet in a problem (mostly "how do I..." questions). Not verified: GUI-behaviour items (the "Restore Defaults" flow
was redesigned upstream; needs a running GUI), #94 autoload discoverability, #270 BTN_BACK naming. The 259 PRs are still unread; reading them would link fixes to issues.

**PR candidates, in order of evidence:** (1) uinput module: modules-load.d entry plus README note; (2) FAQ entry for the per-app switching limit; (3) contributed OpenRC/runit
scripts (needs testers). None has been opened.
