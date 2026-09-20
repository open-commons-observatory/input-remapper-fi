# Presets that follow the focused application are impossible on Wayland, and the docs do not say so

`problem` · status `open` · 7 evidence items · [Back to the register](../register.md)

Users keep asking for presets that switch by focused application or window (seven items over five years). The maintainer answers each time that Wayland hides window focus, so it cannot work on every desktop. Verified at upstream cb8f5fd: README, usage.md and examples.md do not state this limit or the workaround (input-remapper-control bound to a desktop shortcut, or an X11 window-watcher script). Candidate PR: an FAQ entry. The feature itself is not being asked of the maintainer.

| Facet | Values |
|---|---|
| change_type | perfective |
| conf | inferred |
| dimension | information-technology, partners |
| effort | small |
| quality | interaction-capability |
| risk | low |
| value | medium |

## Evidence

| Item | State | Title | Summary |
|---|---|---|---|
| [#32](https://github.com/sezanzeb/input-remapper/issues/32) | CLOSED | [Feature Request]: presets assigned to programs | Request for per-application preset switching (e.g. game-specific layouts). Maintainer noted Wayland hides window focus info; possible to implement by watching process names but requires design. Still… |
| [#50](https://github.com/sezanzeb/input-remapper/issues/50) | CLOSED | Suggestion: Any plans on adding focus dependant configurations ? | Request for focus-dependent preset switching. Same Wayland limitation as #32: window focus not accessible via Wayland. Wontfix for Wayland; possible with X11 workarounds. |
| [#56](https://github.com/sezanzeb/input-remapper/issues/56) | CLOSED | Is there any way to quickly switch between mappings (via cli, etc) or… | How to switch presets per focused application? Maintainer confirmed not possible on Wayland; pointed to CLI docs. Docs gap: FAQ entry for Wayland limitation on per-app presets. |
| [#146](https://github.com/sezanzeb/input-remapper/issues/146) | CLOSED | Restrict mappings to specific applications | Per-application preset switching. Standard answer (sixth time seen): not possible on Wayland, Wayland hides window focus. Maintainer linked to the same discussions (#20, #32, #50, #56). |
| [#196](https://github.com/sezanzeb/input-remapper/issues/196) | CLOSED | Automatically switching layouts | Per-window preset/layout switching. Seventh instance of this wontfix answer on Wayland. |
| [#203](https://github.com/sezanzeb/input-remapper/issues/203) | CLOSED | Auto Profile option | Per-application auto-profile switching. Eighth wontfix on Wayland. Community proposed X11-only script using xdotool; maintainer said CLI + examples.md is the right vehicle for this. |
| [#252](https://github.com/sezanzeb/input-remapper/issues/252) | OPEN | Global profiles + Quick Switching profiles | Global profiles and quick profile switching across multiple devices. Per-app switching reaffirmed as impossible on Wayland without a separate tray tool using CLI. Community suggested a systray tool a… |
