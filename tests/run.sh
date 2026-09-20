#!/usr/bin/env bash
# End-to-end self-test on a fixture. Needs doltgres on PATH (tools/install-doltgres.sh) and pip install -r requirements.txt.
set -euo pipefail
cd "$(dirname "$0")/.."
export ATLAS_HOME="${ATLAS_HOME:-$(mktemp -d)}"
mkdir -p "$ATLAS_HOME"
export ATLAS_DATABASE="atlas_test_$$_$RANDOM"   # private database: safe on a server that already holds data
# The fixture carries its own vocabulary, so this test keeps working in atlases whose taxonomy.yaml differs.
export ATLAS_TAXONOMY="tests/fixtures/taxonomy.yaml"
A="python tools/atlas.py"
fail() { echo "TEST FAILED: $*" >&2; exit 1; }
count() { $A sql "SELECT count(*) AS n FROM analysis" | sed -n 3p | tr -d ' '; }

$A db init
$A acquire --items-json tests/fixtures/items.json --commits-json tests/fixtures/commits.json
[ "$($A next -n 10)" = "1 2 3 5" ] || fail "next must list unread issues and leave PRs out"
$A apply tests/fixtures/batch-ok.tsv
[ "$(count)" = "3" ] || fail "valid batch should give 3 analyses"

BEFORE=$(count)
if $A apply tests/fixtures/batch-bad.tsv 2> "$ATLAS_HOME/bad.err"; then fail "bad batch was accepted"; fi
for msg in "single-valued" "unknown facet" "not in the taxonomy" "not in the database"; do
  grep -q "$msg" "$ATLAS_HOME/bad.err" || fail "expected error text: $msg"
done
[ "$(count)" = "$BEFORE" ] || fail "a rejected batch must not change the database"

$A sql "INSERT INTO problem VALUES ('docs-missing', 'Docs are missing', 'Several items ask questions the docs should answer.', 'open')"
$A sql "INSERT INTO problem_item VALUES ('docs-missing', 1)" --commit "test: register a problem"
if $A sql "INSERT INTO tag VALUES (1, 'kind', 'not-a-kind')" 2>/dev/null; then fail "database accepted a tag outside the taxonomy"; fi

$A check || true
$A status
$A render --out "$ATLAS_HOME/out1"
$A render --out "$ATLAS_HOME/out2"
diff -r "$ATLAS_HOME/out1" "$ATLAS_HOME/out2" >/dev/null || fail "render is not deterministic"
O="$ATLAS_HOME/out1"
for f in index.md coverage.md triage.md problems.md problems/docs-missing.md by/cause/doc-gap.md provenance.md; do test -f "$O/$f" || fail "missing page $f"; done
! grep -rq "built-in method" "$O" || fail "a template read a dict method instead of a column"
grep -q "Docs are missing" "$O/problems.md" || fail "problem not rendered"
grep -q "uninstall" "$O/by/cause/doc-gap.md" || fail "facet page lacks item text"
HASH=$(grep -o 'commit `[0-9a-z]*`' "$O/provenance.md" | grep -o '[0-9a-z]\{12\}')
[ "$(grep -rl "$HASH" "$O" | wc -l)" = "1" ] || fail "the database commit stamp must appear on exactly one page"

$A export --dir "$ATLAS_HOME/e1"; $A export --dir "$ATLAS_HOME/e2"
diff -r "$ATLAS_HOME/e1" "$ATLAS_HOME/e2" >/dev/null || fail "export is not deterministic"
[ ! -d .doltcfg ] || fail "server state leaked into the repository working directory"
$A sql "SELECT 1" >/dev/null   # server still healthy
echo "ALL TESTS PASSED"
