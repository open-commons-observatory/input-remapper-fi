# Asks that upstream already meets

`problem` · status `closed` · 4 evidence items · [Back to the register](../register.md)

Verified at upstream cb8f5fd (2026-09-14): #66 a uinput device name longer than 80 characters is truncated (injector.py: name[:80]); #11 and #81 uninstalling is documented (README: sudo python3 -m install.uninstall); #269 python3-devel is listed in the README dependencies. No PR needed; their pr_potential is re-tagged resolved.

| Facet | Values |
|---|---|
| conf | inferred |

## Evidence

| Item | State | Title | Summary |
|---|---|---|---|
| [#11](https://github.com/sezanzeb/input-remapper/issues/11) | CLOSED | how to remove | Empty issue body; user wanted to know how to uninstall. Maintainer replied with removal commands for apt, pacman, pip. Documentation gap. |
| [#66](https://github.com/sezanzeb/input-remapper/issues/66) | CLOSED | UInputError: uinput device name must not be longer than 80 characters | UInput device name too long (>80 chars) for Microsoft 2.4GHz Transceiver v9.0. Reported then self-resolved. PR potential: truncate device names to 80 chars in uinput creation. |
| [#81](https://github.com/sezanzeb/input-remapper/issues/81) | CLOSED | Uninstalling when setup.py was used? | How to uninstall when setup.py was used (not apt/pip). Maintainer provided workaround (find + rm). setup.py removed from docs. Docs gap: uninstall instructions for unusual install methods. |
| [#269](https://github.com/sezanzeb/input-remapper/issues/269) | CLOSED | Add python3-devel requirement to installation instructions for pip | python3-devel not mentioned in pip install instructions for Fedora. Maintainer added the note to the README. |
