# kind: `meta`

about the project itself (governance, naming, packaging)

14 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#40](https://github.com/sezanzeb/input-remapper/issues/40) | CLOSED | Packing via debian/rules | Request for Debian-compliant packaging (dpkg-buildpackage). A Debian Developer volunteered, built the package, submitted to NEW queue. key-mapper 1.0.0 accepted into Debian 12. |
| [#42](https://github.com/sezanzeb/input-remapper/issues/42) | CLOSED | Generating xkb configs | Design notes issue (by maintainer) for XKB config generation to support unknown keys. Covers setxkbmap crash risks and difficulty of writing valid XKB files. Internal planning issue. |
| [#70](https://github.com/sezanzeb/input-remapper/issues/70) | CLOSED | Hi, I did some work on another project you might find helpful | External contributor shared a related project (evdevremapkeys) with potentially helpful patterns: static binary building, systemd user service, and udev uaccess rules for device permissions. |
| [#83](https://github.com/sezanzeb/input-remapper/issues/83) | CLOSED | rpm-package | Request for RPM packaging for Fedora. Community members contributed COPR repo and spec file discussions. Also surfaces python-evdev upstream maintenance concern (gvalkov). Maintainer added as co-main… |
| [#147](https://github.com/sezanzeb/input-remapper/issues/147) | OPEN | Help wanted from people who know X/Gnome/Wayland/KDE internals | Meta issue: maintainer asking for help from X/GNOME/Wayland/KDE internals experts. Lists all known environment-incompatibility problems that are in the DE's territory. Confirms a cluster of issues ma… |
| [#177](https://github.com/sezanzeb/input-remapper/issues/177) | OPEN | Ways to help | Help wanted document: lists ways to contribute (answer discussions, translations, provide a device for testing, help with X11/GNOME internals). Meta issue. |
| [#191](https://github.com/sezanzeb/input-remapper/issues/191) | CLOSED | Translations for offline docs | Discussion about offline vs online docs for macro reference, especially for i18n purposes. Decided to link online English docs from the help window for now. |
| [#192](https://github.com/sezanzeb/input-remapper/issues/192) | OPEN | using ID_INPUT_* attributes of devices | Technical investigation: should key-mapper use ID_INPUT_* udev attributes (via pyudev) instead of its own classify() function for device type detection? Would make classification match what GNOME/KDE… |
| [#218](https://github.com/sezanzeb/input-remapper/issues/218) | CLOSED | Rename to "keycode-mapper"? | Project rename discussion: "key-mapper" → "Input Remapper". Community preferred "Input Remapper" over "Keycode Mapper". Renamed in 1.3.0. GitHub redirects handle old links. Also drove the Python pack… |
| [#246](https://github.com/sezanzeb/input-remapper/issues/246) | CLOSED | Improve tests | Test infrastructure improvement issue: toolbox module, cleanup helpers, timing-tolerant tests, integration vs unit split. jonasBoss proposed improvements. Long ongoing discussion about test architect… |
| [#248](https://github.com/sezanzeb/input-remapper/issues/248) | CLOSED | Key Mapper was renamed to Input Remapper | Announcement: project renamed from "key-mapper" to "input-remapper" as of 1.3.0. AUR package migration note. Python package renamed to input_remapper. GitHub repo redirect active. |
| [#253](https://github.com/sezanzeb/input-remapper/issues/253) | CLOSED | failing tests in main branche | Test failures in main branch: GUI tests fail when run from PyCharm because the test window doesn't get focus in some DE configurations. Fixed by adding PyCharm run configuration for tests. |
| [#266](https://github.com/sezanzeb/input-remapper/issues/266) | CLOSED | Run unittests via ci pipeline | Run unit tests via CI pipeline. Contributor offered to set up GitHub Actions. Eventually implemented. |
| [#283](https://github.com/sezanzeb/input-remapper/issues/283) | CLOSED | Add pydantic dependency to aur, readme and deb | Reminder to add pydantic to AUR, README, and deb dependencies after its addition to the codebase. |
