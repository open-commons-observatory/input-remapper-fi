# Only a systemd unit ships; no OpenRC, runit or sysv scripts

`problem` · status `open` · 2 evidence items · [Back to the register](../register.md)

Only data/input-remapper.service ships, so the daemon cannot be autostarted on OpenRC, runit or sysv systems (Gentoo, Artix, Alpine, postmarketOS). In #15 the maintainer asked for a PR and community members posted working OpenRC and runit scripts in the thread. Verified at upstream cb8f5fd: no OpenRC, runit or sysv files in the repository. Candidate PR: contributed init scripts plus a README section; needs someone who can test on those systems.

| Facet | Values |
|---|---|
| change_type | additive |
| conf | inferred |
| dimension | partners |
| effort | medium |
| quality | compatibility, flexibility |
| risk | low |
| value | medium |

## Evidence

| Item | State | Title | Summary |
|---|---|---|---|
| [#15](https://github.com/sezanzeb/input-remapper/issues/15) | CLOSED | OpenRC init script needed | Request for OpenRC and sysv init scripts. Maintainer asked for a PR; community members posted working OpenRC and runit scripts in comments but no official merge. PR potential: add init scripts to pac… |
| [#122](https://github.com/sezanzeb/input-remapper/issues/122) | CLOSED | rc-service key-mapper start - rc-service: service `key-mapper' does n… | PostmarketOS (non-systemd): rc-service could not find key-mapper. Root: key-mapper's D-Bus setup assumes systemd. Workaround: sudo key-mapper-service -d. Also: uinput module not loaded on phone; modp… |
