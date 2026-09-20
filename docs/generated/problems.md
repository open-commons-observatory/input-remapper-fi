# Problem registry

A problem is a recurring failure with one root cause and (usually) one fix. Many items point at one problem.

| Problem | Status | Items |
|---|---|---|
| [Asks that upstream already meets](problems/already-fixed-or-documented-upstream.md) | closed | 4 |
| [Only a systemd unit ships; no OpenRC, runit or sysv scripts](problems/no-non-systemd-init-scripts.md) | open | 2 |
| [Presets that follow the focused application are impossible on Wayland, and the…](problems/per-app-switching-wayland.md) | open | 7 |
| [Requested features still missing upstream (each a separate PR)](problems/requested-features-still-missing.md) | open | 5 |
| [Injection fails when the uinput kernel module is not loaded](problems/uinput-module-not-loaded.md) | open | 3 |

## Actionable items not yet assigned to a problem (52)

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
| [#195](https://github.com/sezanzeb/input-remapper/issues/195) | docs-fix | some mappings not available |
| [#199](https://github.com/sezanzeb/input-remapper/issues/199) | docs-fix | Buttons suddenly unrecognized |
| [#208](https://github.com/sezanzeb/input-remapper/issues/208) | docs-fix | key-mapper.service start operation timed out. Terminating. |
| [#209](https://github.com/sezanzeb/input-remapper/issues/209) | docs-fix | Can we map a key to arbitrary unicode char? |
| [#210](https://github.com/sezanzeb/input-remapper/issues/210) | docs-fix | Cyrillic symbols not getting injected |
| [#212](https://github.com/sezanzeb/input-remapper/issues/212) | docs-fix | Autoloading not working on sway |
| [#226](https://github.com/sezanzeb/input-remapper/issues/226) | docs-fix | Getting Confusing Feedback |
| [#238](https://github.com/sezanzeb/input-remapper/issues/238) | docs-fix | key-mapper does not work in all software, but why? |
| [#242](https://github.com/sezanzeb/input-remapper/issues/242) | docs-fix | F11 + shift_L or F11 + shift_R |
| [#243](https://github.com/sezanzeb/input-remapper/issues/243) | docs-fix | Home row mods fine tune |
| [#268](https://github.com/sezanzeb/input-remapper/issues/268) | docs-fix | Key-Mapper |
| [#270](https://github.com/sezanzeb/input-remapper/issues/270) | docs-fix | `BTN_BACK` and `BTN_FORWARD` seem to do nothing |
