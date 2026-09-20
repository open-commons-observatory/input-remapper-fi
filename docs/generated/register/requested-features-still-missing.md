# Requested features still missing upstream (each a separate PR)

`request` · status `open` · 5 evidence items · [Back to the register](../register.md)

Open requests verified absent at upstream cb8f5fd: a text() macro (#173), an LED macro (#160; a contributor started a branch), udev-based device classification (#192), search or filter of the mapping list (#207), desktop notifications when a device is mapped (#116). These are separate PRs, grouped only because each is a small missing feature.

| Facet | Values |
|---|---|
| change_type | additive |
| conf | inferred |
| dimension | information-technology |
| effort | medium |
| quality | functional-suitability |
| risk | low |
| value | medium |

## Evidence

| Item | State | Title | Summary |
|---|---|---|---|
| [#116](https://github.com/sezanzeb/input-remapper/issues/116) | OPEN | Notification for device being added/removed/mapped | Desktop notification when a device is mapped/unmapped. Maintainer noted it might be possible via gi/GNOME Notify from the udev handler. Still open. |
| [#160](https://github.com/sezanzeb/input-remapper/issues/160) | OPEN | Request: LED control | LED control in macros (Num/Caps/Scroll lock LEDs). Maintainer left design notes; contributor started working on it via EV_LED injection. PR in progress on a branch. Contributor ran into asyncio compl… |
| [#173](https://github.com/sezanzeb/input-remapper/issues/173) | OPEN | Add more user-friendly syntax for generating a series of keystrokes | text() macro: type a string of characters instead of k(a).k(b).k(c)... Maintainer pointed to where to contribute; partial implementation notes. PR potential: add text() macro function with simple ASC… |
| [#192](https://github.com/sezanzeb/input-remapper/issues/192) | OPEN | using ID_INPUT_* attributes of devices | Technical investigation: should key-mapper use ID_INPUT_* udev attributes (via pyudev) instead of its own classify() function for device type detection? Would make classification match what GNOME/KDE… |
| [#207](https://github.com/sezanzeb/input-remapper/issues/207) | OPEN | Filtering/searching the mapping table | Search/filter the mapping table. For users with many mappings. Maintainer proposed jump-to-match style. PR potential: add search field that filters or jumps to mappings. |
