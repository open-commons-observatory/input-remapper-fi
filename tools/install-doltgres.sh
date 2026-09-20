#!/bin/sh
# Install the pinned Doltgres release. Usage: tools/install-doltgres.sh [dest-dir]  (default ~/.local/bin)
set -eu
V="${DOLTGRES_VERSION:-$(sed -n 's/^doltgres_version: *//p' "$(dirname "$0")/../atlas.yaml")}"
DEST="${1:-$HOME/.local/bin}"
case "$(uname -s)" in Linux) os=linux;; Darwin) os=darwin;; *) echo "unsupported OS" >&2; exit 1;; esac
case "$(uname -m)" in x86_64|amd64) arch=amd64;; aarch64|arm64) arch=arm64;; *) echo "unsupported CPU" >&2; exit 1;; esac
tmp="$(mktemp -d)"
curl -fsSL -o "$tmp/dg.tgz" "https://github.com/dolthub/doltgresql/releases/download/$V/doltgresql-$os-$arch.tar.gz"
tar xzf "$tmp/dg.tgz" -C "$tmp"
mkdir -p "$DEST" && cp "$tmp"/doltgresql-*/bin/doltgres "$DEST/doltgres"
echo "installed doltgres $V to $DEST/doltgres"
