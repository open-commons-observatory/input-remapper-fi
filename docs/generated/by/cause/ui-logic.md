# cause: `ui-logic`

GTK UI logic or state management defect

4 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#10](https://github.com/sezanzeb/input-remapper/issues/10) | CLOSED | GUI unresponsive | GUI freezes on Arch (no error, just unresponsive). User also wanted Capslock+vim key combinations which were not yet implemented. Maintainer implemented combinations in 0.5.0; freeze symptom carried… |
| [#44](https://github.com/sezanzeb/input-remapper/issues/44) | CLOSED | Can't create another remapping without saving and change profile firs… | UI bug on Fedora/KDE main branch: Add mapping row button disappeared after first remap. Not reproducible by the end; maintainer added extra guard logic for consistency checking. |
| [#123](https://github.com/sezanzeb/input-remapper/issues/123) | CLOSED | Multiple devices with same name share the same macros | Two identical joysticks (Thrustmaster T.16000M) share the same preset files. User confused that selecting device 2 shows device 1's mappings. Maintainer explained design: presets shared by model, dif… |
| [#247](https://github.com/sezanzeb/input-remapper/issues/247) | CLOSED | Renaming the preset in the gui does not update the preset in the auto… | Renaming a preset in the GUI does not update the autoload entry in config.json. The old preset name stays in autoload; injection therefore silently uses the old name. Maintainer confirmed and fixed. |
