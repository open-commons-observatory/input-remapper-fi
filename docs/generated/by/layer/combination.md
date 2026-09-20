# layer: `combination`

key combination detection and matching

5 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#10](https://github.com/sezanzeb/input-remapper/issues/10) | CLOSED | GUI unresponsive | GUI freezes on Arch (no error, just unresponsive). User also wanted Capslock+vim key combinations which were not yet implemented. Maintainer implemented combinations in 0.5.0; freeze symptom carried… |
| [#30](https://github.com/sezanzeb/input-remapper/issues/30) | CLOSED | Caps Lock as Escape and Control | Request for dual-function Capslock: Escape when tapped, Ctrl when held with another key. Maintainer explained it was architecturally complex (needs key-state awareness and arbitrary-key combos). Late… |
| [#49](https://github.com/sezanzeb/input-remapper/issues/49) | CLOSED | space on release if not part of combination + input lags | Request for space-as-modifier: Space=Space when tapped but Space+J=Left etc. when combined. Complex feature; maintainer explained architectural difficulty. Eventually solved via set/ifeq macros and l… |
| [#159](https://github.com/sezanzeb/input-remapper/issues/159) | CLOSED | [Req] Priority setting / Ordering precedence of mappings | Combination release fires the base key even when a chord was used (fn3 → BTN_MIDDLE fires on fn3 release regardless). Maintainer explained this is expected: combination does not consume the base key'… |
| [#242](https://github.com/sezanzeb/input-remapper/issues/242) | CLOSED | F11 + shift_L or F11 + shift_R | Water-damaged keyboard: F11+Shift maps to repeated characters. Root: F11 is forwarded before the combination triggers; must also map F11 to disable to suppress it. Combination behavior: base key is a… |
