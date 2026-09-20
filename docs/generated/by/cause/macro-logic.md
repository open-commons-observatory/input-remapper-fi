# cause: `macro-logic`

bug in macro expression parsing or execution

7 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#46](https://github.com/sezanzeb/input-remapper/issues/46) | CLOSED | Tartarus v2 key button stuck/repeats (Manjaro, OpenRazer) | Razer Tartarus V2 on Manjaro with OpenRazer: mapped macro kept key pressed after button release (key-up not triggered). Maintainer pushed fix; workaround was to use m(ctrl, k(v)) syntax instead of co… |
| [#47](https://github.com/sezanzeb/input-remapper/issues/47) | CLOSED | v0.7.0 using Key + Key vs macros | REL_HWHEEL mapped to super+next/prior: scroll continued repeating after mouse button release. Root: early 0.7.0 release had a fix not yet in the .deb; installing the re-released .deb resolved it. Scr… |
| [#59](https://github.com/sezanzeb/input-remapper/issues/59) | CLOSED | Key won't release | Keys stuck/repeating after injection: mapped key kept sending repeat events. Maintainer pushed fix to main. Side discussion: writing characters from a non-default keyboard layout requires xkb work; w… |
| [#162](https://github.com/sezanzeb/input-remapper/issues/162) | CLOSED | Hold-keystroke doesn't work with mouse click | h(k(BTN_MOUSE)) fires clicks too fast; environment batches them so only one click is perceived. Workaround: h(k(BTN_MOUSE).w(500)) adds a delay. Environment coalesces rapid mouse button events. Docs… |
| [#200](https://github.com/sezanzeb/input-remapper/issues/200) | CLOSED | Wheel mapping stopped working, propagates only once | Mouse wheel mapped buttons only scroll once then stop responding for ~30 seconds. Looks like a timing or release-event bug in scroll event injection. Logs shared but no fix visible. |
| [#201](https://github.com/sezanzeb/input-remapper/issues/201) | CLOSED | Holding modifier stops modifying after combination macro | Holding Shift+mapped combination: after the combo macro runs, subsequent unmapped keys lose the shift modifier. Root: k(Shift_L) in macro sends complete press+release, so shift is down on the "forwar… |
| [#229](https://github.com/sezanzeb/input-remapper/issues/229) | CLOSED | Combinations involving Modifiers on Wayland. Modifier key not release… | Wayland: modifier key in combination not released after macro. Same root as #221. Maintainer confirmed fix in key-mapper-devices branch. release_all() macro proposed as a cleaner solution; key_up() a… |
