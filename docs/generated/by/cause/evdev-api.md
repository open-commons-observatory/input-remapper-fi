# cause: `evdev-api`

evdev API usage or kernel evdev behaviour

4 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#23](https://github.com/sezanzeb/input-remapper/issues/23) | CLOSED | key-mapper.service fails | Service crashed at startup on Ubuntu 20.10 with NameError in evdev 1.3.0 ecodes.py. Workaround: reinstall evdev via pip not setuptools. Reported to python-evdev upstream. Maintainer says use evdev fr… |
| [#27](https://github.com/sezanzeb/input-remapper/issues/27) | CLOSED | Key Mapper can't map brightness keys | Brightness keys (KEY_BRIGHTNESSDOWN/UP) do not report events via evdev on the user's MX Linux/xfce laptop even though the device appears to have the capability. Maintainer confirmed this is an evdev/… |
| [#208](https://github.com/sezanzeb/input-remapper/issues/208) | CLOSED | key-mapper.service start operation timed out. Terminating. | Service startup timed out. Likely python-evdev compilation issue (same as #23 cluster). Maintainer recommended using distro package (python-evdev from pacman/apt) instead of pip-compiled version. |
| [#282](https://github.com/sezanzeb/input-remapper/issues/282) | OPEN | Mouse wheel events not working when cursor is moving | Scroll events from mapped keys blocked by libinput when mouse cursor is moving simultaneously. Works in Firefox (GTK) but not in GNOME Shell apps (Qt/non-GTK). Root: libinput likely filters scroll ev… |
