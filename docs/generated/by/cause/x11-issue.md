# cause: `x11-issue`

X11-specific behaviour (XInput, XTest, XKB)

12 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#33](https://github.com/sezanzeb/input-remapper/issues/33) | CLOSED | key_f13 -> key_f24 seem to be incorrect | F13-F24 and unusual keys not mappable because xmodmap/xkb didn't know about them. Maintainer explored xkb branch but hit libxkbcommon issues on some systems. Workaround: use macro for unsupported key… |
| [#42](https://github.com/sezanzeb/input-remapper/issues/42) | CLOSED | Generating xkb configs | Design notes issue (by maintainer) for XKB config generation to support unknown keys. Covers setxkbmap crash risks and difficulty of writing valid XKB files. Internal planning issue. |
| [#114](https://github.com/sezanzeb/input-remapper/issues/114) | OPEN | xmodmap on wayland | ~/.Xmodmap interferes with key-mapper on Wayland in KDE Plasma: key-mapper uses xmodmap -pke to build the key name list, which is wrong when Xmodmap has been applied. On Wayland the Xmodmap file has… |
| [#126](https://github.com/sezanzeb/input-remapper/issues/126) | CLOSED | How to map ctrl hjkl as arrow keys | ctrl+hjkl as arrow keys fails because ctrl modifier state is passed through to injected keys (ctrl+left = word-skip). Solution: also disable ctrl_l in the mapping or map it to ctrl_l with combination… |
| [#145](https://github.com/sezanzeb/input-remapper/issues/145) | CLOSED | XCompose being ignored | ~/.XCompose rules ignored while key-mapper daemon is active. Root: XCompose applies to specific X11 device IDs; key-mapper's virtual injection device gets a new ID not covered by XCompose config. Sam… |
| [#152](https://github.com/sezanzeb/input-remapper/issues/152) | CLOSED | Layout is changed on Apply | Applying a preset changes the keyboard layout to German on a US+German locale system. Root: X11/GNOME assigns a keyboard layout to the new virtual uinput device based on system locale; key-mapper has… |
| [#155](https://github.com/sezanzeb/input-remapper/issues/155) | CLOSED | Key mapping not working, nothing happens | Modifier key used in combination source leaks through to output (Alt+j mapped to Down, but Alt is still held → Alt+Down in browser). Documented behavior: must also disable or remap the modifier key.… |
| [#210](https://github.com/sezanzeb/input-remapper/issues/210) | CLOSED | Cyrillic symbols not getting injected | Cyrillic symbols and tilde (~) not mappable directly on Linux Mint/Cinnamon with Russian+English layout. Root: xmodmap-based key names depend on active layout; tilde not in xmodmap output. Maintainer… |
| [#220](https://github.com/sezanzeb/input-remapper/issues/220) | OPEN | xmodmap should be a recommended dependency | xmodmap should be a recommended dependency; without it, mapping by key name (e.g. "a") fails because xmodmap -pke provides the key name lookup. Maintainer agreed to document it; AUR package added it… |
| [#221](https://github.com/sezanzeb/input-remapper/issues/221) | CLOSED | Using Control_L + Alt_L as modifiers requires a waiting time for key… | Wayland: modifier key not released after combination macro (Control_L + combo). Root: modifier injected via forwarded device can't be released by mapped device. Fix in key-mapper-devices branch: glob… |
| [#241](https://github.com/sezanzeb/input-remapper/issues/241) | CLOSED | Alt + left shortcut | Alt+Left mapped to mouse button 6 not working as expected. Long debug session; user has difficulty with evtest. Maintainer asked for evtest output from both the original device and key-mapper device.… |
| [#258](https://github.com/sezanzeb/input-remapper/issues/258) | OPEN | Alphanumeric events not working without prefixing KEY_ | Alphanumeric keys stopped working without KEY_ prefix after migrating config to new install. Root: xmodmap.json was empty (copied from previous system where it may have been populated differently). i… |
