# layer: `config`

configuration and preset files (storage, migration, format)

8 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#4](https://github.com/sezanzeb/input-remapper/issues/4) | CLOSED | add support for non-GUI | Request for tty/non-GUI mode. Maintainer stated it was achievable; implemented CLI via key-mapper-control and D-Bus in 0.4.0. Side discussion of X11 xmodmap for cedilla layout. |
| [#8](https://github.com/sezanzeb/input-remapper/issues/8) | CLOSED | Mappings not autoloaded | Mappings not surviving reboot on Manjaro GNOME. Three overlapping bugs: service not enabled by installer, config.json path-resolution corruption, and GNOME autostart .desktop missing Type=Application… |
| [#67](https://github.com/sezanzeb/input-remapper/issues/67) | CLOSED | [Request] Version Command line Argument | Request for --version CLI argument. Already implemented on a branch about to be released. |
| [#93](https://github.com/sezanzeb/input-remapper/issues/93) | CLOSED | Unable to configure devices with the same name independently | Two identical gamepads (SPEEDLINK TORID) with separate USB receivers shown as one device in the UI. Root: device deduplication used only name, not physical path. Fixed in getdevices-duplicate-2 branc… |
| [#123](https://github.com/sezanzeb/input-remapper/issues/123) | CLOSED | Multiple devices with same name share the same macros | Two identical joysticks (Thrustmaster T.16000M) share the same preset files. User confused that selecting device 2 shows device 1's mappings. Maintainer explained design: presets shared by model, dif… |
| [#246](https://github.com/sezanzeb/input-remapper/issues/246) | CLOSED | Improve tests | Test infrastructure improvement issue: toolbox module, cleanup helpers, timing-tolerant tests, integration vs unit split. jonasBoss proposed improvements. Long ongoing discussion about test architect… |
| [#247](https://github.com/sezanzeb/input-remapper/issues/247) | CLOSED | Renaming the preset in the gui does not update the preset in the auto… | Renaming a preset in the GUI does not update the autoload entry in config.json. The old preset name stays in autoload; injection therefore silently uses the old name. Maintainer confirmed and fixed. |
| [#253](https://github.com/sezanzeb/input-remapper/issues/253) | CLOSED | failing tests in main branche | Test failures in main branch: GUI tests fail when run from PyCharm because the test window doesn't get focus in some DE configurations. Fixed by adding PyCharm run configuration for tests. |
