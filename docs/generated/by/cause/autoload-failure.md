# cause: `autoload-failure`

device plug/unplug autoloading of presets not working (very common cluster)

9 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#8](https://github.com/sezanzeb/input-remapper/issues/8) | CLOSED | Mappings not autoloaded | Mappings not surviving reboot on Manjaro GNOME. Three overlapping bugs: service not enabled by installer, config.json path-resolution corruption, and GNOME autostart .desktop missing Type=Application… |
| [#25](https://github.com/sezanzeb/input-remapper/issues/25) | CLOSED | Automatically loading for bluetooth devices | Bluetooth devices not autoloaded on reconnect (Ubuntu 20.10 GNOME, Logitech M585 and K380). Service could not inject for unknown device at login time. Fixed in 0.7.0 via udev rule: autoload triggers… |
| [#57](https://github.com/sezanzeb/input-remapper/issues/57) | CLOSED | Automatic reapplying mappings on device reconnect | Mappings not reapplied when device is unplugged and replugged. Reporter updated to 0.7.0 to check; no follow-up. Autoload-on-reconnect behavior was supposed to be addressed in 0.7.0 udev fix; edge ca… |
| [#107](https://github.com/sezanzeb/input-remapper/issues/107) | CLOSED | Autoload function not working | Autoload not working on Arch+GNOME 40 after reboot (0.8.1). Multiple debug rounds; root cause was a race: udev-triggered autoload fired before user session was ready. Maintainer found and pushed fix.… |
| [#140](https://github.com/sezanzeb/input-remapper/issues/140) | OPEN | key-mapper freezes external usb mouse and keyboard | External USB devices freeze in GNOME after key-mapper restarts injection (e.g. on USB hub reconnect). evtest shows events being written correctly; GNOME stops accepting them. Autoload via udev rule m… |
| [#154](https://github.com/sezanzeb/input-remapper/issues/154) | CLOSED | Autoload doesn't seem to work, but apply works fine | Autoload not working on startup; Razer Tartarus. Device path mixed up at login (NVidia device in event6 conflicting). Eventually resolved on its own; suspicion of a timing issue. Pattern: device path… |
| [#197](https://github.com/sezanzeb/input-remapper/issues/197) | CLOSED | Keyboard/mouse not working after reboot on arch based distros | Arch/KDE+Bluetooth: keyboard and mouse stop working after reboot until udev timeout expires. Root: udev rule fires key-mapper-control before the service is ready to accept D-Bus connections; D-Bus ca… |
| [#212](https://github.com/sezanzeb/input-remapper/issues/212) | CLOSED | Autoloading not working on sway | Sway on Arch: autoloading on startup not working. Root: Sway affects environment variables that some systemd units depend on for X/Wayland detection; key-mapper-service starts before Sway but the .de… |
| [#274](https://github.com/sezanzeb/input-remapper/issues/274) | OPEN | Buttons do not work after restart | Logitech MX Anywhere 2 Bluetooth: autoload doesn't work after reboot on Ubuntu. Multiple reporters. Root: udev rule fires with empty DEVNAME for Bluetooth devices; service doesn't find device at the… |
