# cause: `wayland-issue`

Wayland-specific behaviour or missing protocol support

12 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#32](https://github.com/sezanzeb/input-remapper/issues/32) | CLOSED | [Feature Request]: presets assigned to programs | Request for per-application preset switching (e.g. game-specific layouts). Maintainer noted Wayland hides window focus info; possible to implement by watching process names but requires design. Still… |
| [#50](https://github.com/sezanzeb/input-remapper/issues/50) | CLOSED | Suggestion: Any plans on adding focus dependant configurations ? | Request for focus-dependent preset switching. Same Wayland limitation as #32: window focus not accessible via Wayland. Wontfix for Wayland; possible with X11 workarounds. |
| [#56](https://github.com/sezanzeb/input-remapper/issues/56) | CLOSED | Is there any way to quickly switch between mappings (via cli, etc) or… | How to switch presets per focused application? Maintainer confirmed not possible on Wayland; pointed to CLI docs. Docs gap: FAQ entry for Wayland limitation on per-app presets. |
| [#114](https://github.com/sezanzeb/input-remapper/issues/114) | OPEN | xmodmap on wayland | ~/.Xmodmap interferes with key-mapper on Wayland in KDE Plasma: key-mapper uses xmodmap -pke to build the key name list, which is wrong when Xmodmap has been applied. On Wayland the Xmodmap file has… |
| [#124](https://github.com/sezanzeb/input-remapper/issues/124) | CLOSED | Feature request: trackball scroll wheel emulation | Trackball scroll-wheel emulation: gsettings scroll-wheel-emulation-button not compatible with key-mapper virtual devices on Wayland. Root: gsettings applies to physical devices, not to key-mapper's v… |
| [#146](https://github.com/sezanzeb/input-remapper/issues/146) | CLOSED | Restrict mappings to specific applications | Per-application preset switching. Standard answer (sixth time seen): not possible on Wayland, Wayland hides window focus. Maintainer linked to the same discussions (#20, #32, #50, #56). |
| [#196](https://github.com/sezanzeb/input-remapper/issues/196) | CLOSED | Automatically switching layouts | Per-window preset/layout switching. Seventh instance of this wontfix answer on Wayland. |
| [#203](https://github.com/sezanzeb/input-remapper/issues/203) | CLOSED | Auto Profile option | Per-application auto-profile switching. Eighth wontfix on Wayland. Community proposed X11-only script using xdotool; maintainer said CLI + examples.md is the right vehicle for this. |
| [#221](https://github.com/sezanzeb/input-remapper/issues/221) | CLOSED | Using Control_L + Alt_L as modifiers requires a waiting time for key… | Wayland: modifier key not released after combination macro (Control_L + combo). Root: modifier injected via forwarded device can't be released by mapped device. Fix in key-mapper-devices branch: glob… |
| [#229](https://github.com/sezanzeb/input-remapper/issues/229) | CLOSED | Combinations involving Modifiers on Wayland. Modifier key not release… | Wayland: modifier key in combination not released after macro. Same root as #221. Maintainer confirmed fix in key-mapper-devices branch. release_all() macro proposed as a cleaner solution; key_up() a… |
| [#252](https://github.com/sezanzeb/input-remapper/issues/252) | OPEN | Global profiles + Quick Switching profiles | Global profiles and quick profile switching across multiple devices. Per-app switching reaffirmed as impossible on Wayland without a separate tray tool using CLI. Community suggested a systray tool a… |
| [#261](https://github.com/sezanzeb/input-remapper/issues/261) | OPEN | Ship keycode-symbol mapping files for various locales for systems wit… | Ship locale-specific keycode-to-symbol mapping files for systems without xmodmap (especially Wayland). Maintainer noted maintaining per-locale files would be complex; each DE has its own Wayland layo… |
