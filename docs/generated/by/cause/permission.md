# cause: `permission`

missing udev rules, uinput device access, group membership

12 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#2](https://github.com/sezanzeb/input-remapper/issues/2) | CLOSED | AUR still broken | AUR install failed because plugdev group did not exist on some Manjaro configs; maintainer patched service to handle missing group. Also contains an early feature request for gamepad axis mapping. |
| [#19](https://github.com/sezanzeb/input-remapper/issues/19) | CLOSED | App doesn't open on ZOrin OS | ZorinOS: app did not open from menu and user unclear about password prompt (polkit). Maintainer walked through install and confirmed a recent fix resolved it. |
| [#21](https://github.com/sezanzeb/input-remapper/issues/21) | CLOSED | Installing as Flatpak from Flathub | Request for Flatpak on Flathub. Maintainer investigated; Flatpak cannot grant /dev/uinput access due to sandbox restrictions. Fundamental limitation confirmed by flatpak issue #4137. Wontfix. |
| [#29](https://github.com/sezanzeb/input-remapper/issues/29) | CLOSED | could not open uinput device in write mode | Could not open uinput device in write mode. Multiple reporters on Arch. Workaround: install xf86-input-evdev to ensure uinput module loads; also modprobe uinput. Maintainer noted the uinput kernel mo… |
| [#43](https://github.com/sezanzeb/input-remapper/issues/43) | CLOSED | Authentication method doens't work on main. | Fedora 33 + KDE Plasma 5.21: pkexec authentication fails after Plasma upgrade. Reporter closed as a Plasma-specific issue. Not a key-mapper bug. |
| [#117](https://github.com/sezanzeb/input-remapper/issues/117) | CLOSED | Fails to run without policykit? | Sway/Wayland on Arch: no graphical polkit agent installed so key-mapper-gtk pkexec fails silently. Workaround: sudo -E input-remapper-gtk. Docs gap: mention graphical polkit agent requirement for Way… |
| [#122](https://github.com/sezanzeb/input-remapper/issues/122) | CLOSED | rc-service key-mapper start - rc-service: service `key-mapper' does n… | PostmarketOS (non-systemd): rc-service could not find key-mapper. Root: key-mapper's D-Bus setup assumes systemd. Workaround: sudo key-mapper-service -d. Also: uinput module not loaded on phone; modp… |
| [#125](https://github.com/sezanzeb/input-remapper/issues/125) | CLOSED | Cursor not moving in postmarketos | PostmarketOS continuation: cursor not moving because the phone has no EV_REL-capable device after injection. Maintainer confirmed this is outside scope; user eventually resolved partial functionality. |
| [#181](https://github.com/sezanzeb/input-remapper/issues/181) | CLOSED | Error trying to install on Fedora 34 | Fedora 34: pip install evdev fails without python3-devel. Also: setup.py installs service file to wrong path on Fedora (not found by systemd). Multiple reporters. Community workaround: install python… |
| [#184](https://github.com/sezanzeb/input-remapper/issues/184) | CLOSED | polkit-agent-helper-1: pam_authenticate failed: Permission denied | polkit-agent-helper-1 pam_authenticate failed on Arch+X11. Maintainer asked if pkexec works for any other app; no follow-up. Likely a local PAM/polkit config issue. |
| [#217](https://github.com/sezanzeb/input-remapper/issues/217) | CLOSED | Can't open the GUI if user is not part of the "input" group | Arch+KDE: pkexec authentication fails with "access denied" even with wheel group membership. Maintainer said this shouldn't be a key-mapper issue; probably a polkit or PAM configuration problem speci… |
| [#256](https://github.com/sezanzeb/input-remapper/issues/256) | CLOSED | could not open uinput device in write mode | Could not open uinput device in write mode (input-remapper 1.x). Maintainer asked for lsmod/uinput status; no follow-up. Redirected to #29. |
