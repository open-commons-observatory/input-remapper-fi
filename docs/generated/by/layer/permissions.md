# layer: `permissions`

udev rules, uinput access, group membership, capabilities

9 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#2](https://github.com/sezanzeb/input-remapper/issues/2) | CLOSED | AUR still broken | AUR install failed because plugdev group did not exist on some Manjaro configs; maintainer patched service to handle missing group. Also contains an early feature request for gamepad axis mapping. |
| [#29](https://github.com/sezanzeb/input-remapper/issues/29) | CLOSED | could not open uinput device in write mode | Could not open uinput device in write mode. Multiple reporters on Arch. Workaround: install xf86-input-evdev to ensure uinput module loads; also modprobe uinput. Maintainer noted the uinput kernel mo… |
| [#115](https://github.com/sezanzeb/input-remapper/issues/115) | CLOSED | Improve README - add note regarding policykit | Add polkit rules note to README so users can skip the password prompt. Maintainer noted security concern (root access without auth = keylogger risk). Commenter noted it's similar to NOPASSWD in sudoe… |
| [#117](https://github.com/sezanzeb/input-remapper/issues/117) | CLOSED | Fails to run without policykit? | Sway/Wayland on Arch: no graphical polkit agent installed so key-mapper-gtk pkexec fails silently. Workaround: sudo -E input-remapper-gtk. Docs gap: mention graphical polkit agent requirement for Way… |
| [#122](https://github.com/sezanzeb/input-remapper/issues/122) | CLOSED | rc-service key-mapper start - rc-service: service `key-mapper' does n… | PostmarketOS (non-systemd): rc-service could not find key-mapper. Root: key-mapper's D-Bus setup assumes systemd. Workaround: sudo key-mapper-service -d. Also: uinput module not loaded on phone; modp… |
| [#125](https://github.com/sezanzeb/input-remapper/issues/125) | CLOSED | Cursor not moving in postmarketos | PostmarketOS continuation: cursor not moving because the phone has no EV_REL-capable device after injection. Maintainer confirmed this is outside scope; user eventually resolved partial functionality. |
| [#184](https://github.com/sezanzeb/input-remapper/issues/184) | CLOSED | polkit-agent-helper-1: pam_authenticate failed: Permission denied | polkit-agent-helper-1 pam_authenticate failed on Arch+X11. Maintainer asked if pkexec works for any other app; no follow-up. Likely a local PAM/polkit config issue. |
| [#217](https://github.com/sezanzeb/input-remapper/issues/217) | CLOSED | Can't open the GUI if user is not part of the "input" group | Arch+KDE: pkexec authentication fails with "access denied" even with wheel group membership. Maintainer said this shouldn't be a key-mapper issue; probably a polkit or PAM configuration problem speci… |
| [#256](https://github.com/sezanzeb/input-remapper/issues/256) | CLOSED | could not open uinput device in write mode | Could not open uinput device in write mode (input-remapper 1.x). Maintainer asked for lsmod/uinput status; no follow-up. Redirected to #29. |
