# cause: `symbol-mapping`

wrong or missing keysym, evdev type or code

6 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#33](https://github.com/sezanzeb/input-remapper/issues/33) | CLOSED | key_f13 -> key_f24 seem to be incorrect | F13-F24 and unusual keys not mappable because xmodmap/xkb didn't know about them. Maintainer explored xkb branch but hit libxkbcommon issues on some systems. Workaround: use macro for unsupported key… |
| [#42](https://github.com/sezanzeb/input-remapper/issues/42) | CLOSED | Generating xkb configs | Design notes issue (by maintainer) for XKB config generation to support unknown keys. Covers setxkbmap crash risks and difficulty of writing valid XKB files. Internal planning issue. |
| [#59](https://github.com/sezanzeb/input-remapper/issues/59) | CLOSED | Key won't release | Keys stuck/repeating after injection: mapped key kept sending repeat events. Maintainer pushed fix to main. Side discussion: writing characters from a non-default keyboard layout requires xkb work; w… |
| [#195](https://github.com/sezanzeb/input-remapper/issues/195) | CLOSED | some mappings not available | Cannot map > or $ characters directly. Maintainer explained: KEY_DOLLAR/KEY_GREATER are kernel codes; whether they produce the symbol depends on the keyboard layout in the environment. Solution: use… |
| [#222](https://github.com/sezanzeb/input-remapper/issues/222) | CLOSED | Detected name showing up as "unknown" in GUI | Logitech G300s button G9 shows as "unknown" in GUI (no human-readable name in xmodmap). Button works but displays as keycode number. PR potential: show keycode number (e.g. "280") instead of "unknown… |
| [#270](https://github.com/sezanzeb/input-remapper/issues/270) | CLOSED | `BTN_BACK` and `BTN_FORWARD` seem to do nothing | BTN_BACK and BTN_FORWARD do nothing for browser navigation. Root: naming in input-event-codes.h is confusing; BTN_SIDE and BTN_EXTRA are what browsers actually use for back/forward. Docs gap: add a n… |
