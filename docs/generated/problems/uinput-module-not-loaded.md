# Injection fails when the uinput kernel module is not loaded

Status: `open`. 3 items. [Back to registry](../problems.md)

Injection fails with "could not open uinput device" when the uinput kernel module is not loaded (reported on Arch and postmarketOS; fixed by running modprobe uinput, sometimes needed after a kernel upgrade). Verified at upstream cb8f5fd: no modprobe, modules-load.d file or troubleshooting note exists in the docs, install scripts, packaging or data/. Candidate PR: ship a modules-load.d entry for uinput with the package and add a troubleshooting note to the README. Not yet tested on a distribution.

| Item | State | Title | Summary |
|---|---|---|---|
| [#29](https://github.com/sezanzeb/input-remapper/issues/29) | CLOSED | could not open uinput device in write mode | Could not open uinput device in write mode. Multiple reporters on Arch. Workaround: install xf86-input-evdev to ensure uinput module loads; also modprobe uinput. Maintainer noted the uinput kernel mo… |
| [#122](https://github.com/sezanzeb/input-remapper/issues/122) | CLOSED | rc-service key-mapper start - rc-service: service `key-mapper' does n… | PostmarketOS (non-systemd): rc-service could not find key-mapper. Root: key-mapper's D-Bus setup assumes systemd. Workaround: sudo key-mapper-service -d. Also: uinput module not loaded on phone; modp… |
| [#256](https://github.com/sezanzeb/input-remapper/issues/256) | CLOSED | could not open uinput device in write mode | Could not open uinput device in write mode (input-remapper 1.x). Maintainer asked for lsmod/uinput status; no follow-up. Redirected to #29. |
