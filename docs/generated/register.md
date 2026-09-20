# Register

Everything worth acting on, in one list (the ITIL 4 *continual improvement register*). Entry types: **problem** (a root cause behind many items),
**request** (a new capability), **improvement** (refactoring, tests, docs, process) and **risk** (something that could hurt the project).
A problem that has a workaround but no fix is a **known error**. Each entry says what kind of change it is ([ISO/IEC/IEEE 14764](../playbook/methodology.md)),
and how much value, effort and risk it carries.

## improvement (3)

| Entry | Status | Change | Value | Effort | Risk | Evidence |
|---|---|---|---|---|---|---|
| [Finish the move to dependency injection so tests become easier to wri…](register/dependency-injection-testability.md) | in-progress | preventive | high | large | medium | 4 |
| [The architecture is hard for newcomers to approach; a contributor gui…](register/architecture-hard-to-approach.md) | open | preventive | medium | medium | low | 3 |
| [Nobody is triaging the open issue backlog](register/backlog-not-triaged.md) | open | - | medium | medium | low | 1 |

## problem (5)

| Entry | Status | Change | Value | Effort | Risk | Evidence |
|---|---|---|---|---|---|---|
| [Asks that upstream already meets](register/already-fixed-or-documented-upstream.md) | closed | - | - | - | - | 4 |
| [Arbitrary characters cannot be injected because the tool sends key co…](register/character-injection-limits.md) | known-error | - | medium | large | medium | 4 |
| [Only a systemd unit ships; no OpenRC, runit or sysv scripts](register/no-non-systemd-init-scripts.md) | open | additive | medium | medium | low | 2 |
| [Presets that follow the focused application are impossible on Wayland…](register/per-app-switching-wayland.md) | open | perfective | medium | small | low | 7 |
| [Injection fails when the uinput kernel module is not loaded](register/uinput-module-not-loaded.md) | open | corrective | medium | small | low | 3 |

## request (2)

| Entry | Status | Change | Value | Effort | Risk | Evidence |
|---|---|---|---|---|---|---|
| [A Qt user interface instead of GTK](register/qt-user-interface.md) | open | additive | medium | large | medium | 3 |
| [Requested features still missing upstream (each a separate PR)](register/requested-features-still-missing.md) | open | additive | medium | medium | low | 5 |

## risk (1)

| Entry | Status | Change | Value | Effort | Risk | Evidence |
|---|---|---|---|---|---|---|
| [The maintainer has largely stepped back; pull-request review is the o…](register/maintainer-stepped-back.md) | open | - | high | large | high | 2 |

## Actionable items not yet in a register entry (49)

| Item | Potential | Title |
|---|---|---|
| [#75](https://github.com/sezanzeb/input-remapper/issues/75) | code-fix | Feature request: refresh list of devices |
| [#83](https://github.com/sezanzeb/input-remapper/issues/83) | code-fix | rpm-package |
| [#88](https://github.com/sezanzeb/input-remapper/issues/88) | code-fix | Pretty printed evdev event output via the GUI |
| [#90](https://github.com/sezanzeb/input-remapper/issues/90) | code-fix | Helper to find symbol names and combinations |
| [#95](https://github.com/sezanzeb/input-remapper/issues/95) | code-fix | Mapping templates |
| [#112](https://github.com/sezanzeb/input-remapper/issues/112) | code-fix | Cannot generate Mouse Button Events |
| [#136](https://github.com/sezanzeb/input-remapper/issues/136) | code-fix | Adding mappings by hitting the output key/combination on any device |
| [#176](https://github.com/sezanzeb/input-remapper/issues/176) | code-fix | Improve combinations involving modifiers |
| [#201](https://github.com/sezanzeb/input-remapper/issues/201) | code-fix | Holding modifier stops modifying after combination macro |
| [#222](https://github.com/sezanzeb/input-remapper/issues/222) | code-fix | Detected name showing up as "unknown" in GUI |
| [#223](https://github.com/sezanzeb/input-remapper/issues/223) | code-fix | Keys on Jabra headphones not detected |
| [#224](https://github.com/sezanzeb/input-remapper/issues/224) | code-fix | Getting the currently injected profile via key-mapper-control |
| [#246](https://github.com/sezanzeb/input-remapper/issues/246) | code-fix | Improve tests |
| [#5](https://github.com/sezanzeb/input-remapper/issues/5) | docs-fix | Can't install on pop!_os 20.10 |
| [#16](https://github.com/sezanzeb/input-remapper/issues/16) | docs-fix | 3 parameter macro |
| [#17](https://github.com/sezanzeb/input-remapper/issues/17) | docs-fix | Wrong user in systemd daemon |
| [#18](https://github.com/sezanzeb/input-remapper/issues/18) | docs-fix | Only works after first unlock |
| [#22](https://github.com/sezanzeb/input-remapper/issues/22) | docs-fix | When to update the software release |
| [#24](https://github.com/sezanzeb/input-remapper/issues/24) | docs-fix | Mouse compatibility |
| [#48](https://github.com/sezanzeb/input-remapper/issues/48) | docs-fix | Systemd service fails on install |
| [#68](https://github.com/sezanzeb/input-remapper/issues/68) | docs-fix | Add ability to reserve key as modifier/disable it completely |
| [#69](https://github.com/sezanzeb/input-remapper/issues/69) | docs-fix | Keys no longer detected in UI after first "apply" |
| [#94](https://github.com/sezanzeb/input-remapper/issues/94) | docs-fix | Key-Mapper Settings Not Persistent |
| [#100](https://github.com/sezanzeb/input-remapper/issues/100) | docs-fix | Feature Request: Distinction between mouse press and mouse release. |
| [#104](https://github.com/sezanzeb/input-remapper/issues/104) | docs-fix | Toggle on/off script needed |
| [#110](https://github.com/sezanzeb/input-remapper/issues/110) | docs-fix | Xinput plugin |
| [#117](https://github.com/sezanzeb/input-remapper/issues/117) | docs-fix | Fails to run without policykit? |
| [#118](https://github.com/sezanzeb/input-remapper/issues/118) | docs-fix | How to edit pressed key without injecting |
| [#123](https://github.com/sezanzeb/input-remapper/issues/123) | docs-fix | Multiple devices with same name share the same macros |
| [#126](https://github.com/sezanzeb/input-remapper/issues/126) | docs-fix | How to map ctrl hjkl as arrow keys |
| [#135](https://github.com/sezanzeb/input-remapper/issues/135) | docs-fix | Document mapping field |
| [#151](https://github.com/sezanzeb/input-remapper/issues/151) | docs-fix | missing macro info ? coming back from #104 |
| [#153](https://github.com/sezanzeb/input-remapper/issues/153) | docs-fix | How to macro an autofire |
| [#155](https://github.com/sezanzeb/input-remapper/issues/155) | docs-fix | Key mapping not working, nothing happens |
| [#159](https://github.com/sezanzeb/input-remapper/issues/159) | docs-fix | [Req] Priority setting / Ordering precedence of mappings |
| [#161](https://github.com/sezanzeb/input-remapper/issues/161) | docs-fix | key-mapper-control doesn't load presets |
| [#162](https://github.com/sezanzeb/input-remapper/issues/162) | docs-fix | Hold-keystroke doesn't work with mouse click |
| [#175](https://github.com/sezanzeb/input-remapper/issues/175) | docs-fix | Can't map wheel click on Razer DeathAdder Chroma |
| [#180](https://github.com/sezanzeb/input-remapper/issues/180) | docs-fix | Can't map broken keys |
| [#191](https://github.com/sezanzeb/input-remapper/issues/191) | docs-fix | Translations for offline docs |
| [#199](https://github.com/sezanzeb/input-remapper/issues/199) | docs-fix | Buttons suddenly unrecognized |
| [#208](https://github.com/sezanzeb/input-remapper/issues/208) | docs-fix | key-mapper.service start operation timed out. Terminating. |
| [#212](https://github.com/sezanzeb/input-remapper/issues/212) | docs-fix | Autoloading not working on sway |
| [#226](https://github.com/sezanzeb/input-remapper/issues/226) | docs-fix | Getting Confusing Feedback |
| [#238](https://github.com/sezanzeb/input-remapper/issues/238) | docs-fix | key-mapper does not work in all software, but why? |
| [#242](https://github.com/sezanzeb/input-remapper/issues/242) | docs-fix | F11 + shift_L or F11 + shift_R |
| [#243](https://github.com/sezanzeb/input-remapper/issues/243) | docs-fix | Home row mods fine tune |
| [#268](https://github.com/sezanzeb/input-remapper/issues/268) | docs-fix | Key-Mapper |
| [#270](https://github.com/sezanzeb/input-remapper/issues/270) | docs-fix | `BTN_BACK` and `BTN_FORWARD` seem to do nothing |
