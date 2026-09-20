# Arbitrary characters cannot be injected because the tool sends key codes, not characters

`problem` · status `known-error` · 4 evidence items · [Back to the register](../register.md)

**Known error.** Workaround until it is fixed: Use the xmodmap-based symbol names, or a macro that holds a modifier while pressing a key that exists in the layout. The Ctrl+Shift+U hex entry works only in some GTK applications and breaks in others.

Several users ask to map a key to a symbol, emoji or non-Latin character. The tool sends kernel key codes and the desktop environment decides which symbol appears, so a character without a key in the active layout cannot be produced reliably (#195, #209, #210). A Unicode-entry macro was shown to be technically possible but declined because it depends on the application (#101). In June 2024 the maintainer said the real fix lies below the tool: the Linux input stack should allow injecting any character instead of any key code, and allow several mapping tools to work on top of each other.

| Facet | Values |
|---|---|
| conf | stated |
| dimension | partners |
| effort | large |
| quality | compatibility, functional-suitability |
| risk | medium |
| value | medium |

## Evidence

| Item | State | Title | Summary |
|---|---|---|---|
| [#101](https://github.com/sezanzeb/input-remapper/issues/101) | CLOSED | unicode macro | Unicode input macro (Ctrl+Shift+U+hex). Maintainer showed it was technically doable but declined: application-dependent behavior (breaks in IntelliJ), not a general solution. |
| [#195](https://github.com/sezanzeb/input-remapper/issues/195) | CLOSED | some mappings not available | Cannot map > or $ characters directly. Maintainer explained: KEY_DOLLAR/KEY_GREATER are kernel codes; whether they produce the symbol depends on the keyboard layout in the environment. Solution: use… |
| [#209](https://github.com/sezanzeb/input-remapper/issues/209) | CLOSED | Can we map a key to arbitrary unicode char? | Can arbitrary Unicode characters (emoji, coins) be mapped? Maintainer explained: key-mapper sends keycodes, environment decides the symbol; no keycode exists for emoji. Workaround: Ctrl+Shift+U+codep… |
| [#210](https://github.com/sezanzeb/input-remapper/issues/210) | CLOSED | Cyrillic symbols not getting injected | Cyrillic symbols and tilde (~) not mappable directly on Linux Mint/Cinnamon with Russian+English layout. Root: xmodmap-based key names depend on active layout; tilde not in xmodmap output. Maintainer… |
