# The architecture is hard for newcomers to approach; a contributor guide and small clean-ups would lower the cost

`improvement` · status `open` · 3 evidence items · [Back to the register](../register.md)

In March 2026 the maintainer wrote that he would welcome contributors but that the architecture and code are very complex, which he attributes to his inexperience at the start, the quirks of the different kinds of input, security (not running everything as root) and Linux integration (udev, autostart, service, D-Bus). The 2021 guide (#177) promises help finding the right place in the code and asks for unit tests, pylint and black. The 2024 macro rework (#1003, merged) shows the direction taken: more classes, judged bulkier than before but worth it. Proposal (the analyst's, not requested by the maintainer): a short architecture guide for contributors covering the service, reader, injector and group concepts, plus small preventive refactors that reduce the entry cost.

| Facet | Values |
|---|---|
| change_type | preventive |
| conf | inferred |
| dimension | information-technology, people |
| effort | medium |
| quality | maintainability |
| risk | low |
| value | medium |

## Evidence

| Item | State | Title | Summary |
|---|---|---|---|
| [#177](https://github.com/sezanzeb/input-remapper/issues/177) | OPEN | Ways to help | Help wanted document: lists ways to contribute (answer discussions, translations, provide a device for testing, help with X11/GNOME internals). Meta issue. |
| [#853](https://github.com/sezanzeb/input-remapper/issues/853) | OPEN | State of Maintenance |  |
| [#1003](https://github.com/sezanzeb/input-remapper/issues/1003) | MERGED | Better macro architecture |  |
