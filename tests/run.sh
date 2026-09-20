#!/usr/bin/env bash
# End-to-end self-test on a fixture. Needs doltgres on PATH (tools/install-doltgres.sh) and pip install -r requirements.txt.
set -euo pipefail
cd "$(dirname "$0")/.."
export FI_HOME="${FI_HOME:-$(mktemp -d)}"
mkdir -p "$FI_HOME"
export FI_DATABASE="fi_test_$$_$RANDOM"   # private database: safe on a server that already holds data
# The fixture carries its own vocabulary, so this test keeps working in FI repositories whose taxonomy.yaml differs.
export FI_TAXONOMY="tests/fixtures/taxonomy.yaml"
export FI_MAINTAINERS="maint"
A="python tools/fi.py"
fail() { echo "TEST FAILED: $*" >&2; exit 1; }
count() { $A sql "SELECT count(*) AS n FROM analysis" | sed -n 3p | tr -d ' '; }

$A db init
$A acquire --items-json tests/fixtures/items.json --commits-json tests/fixtures/commits.json
$A acquire --comments-json tests/fixtures/comments.json --releases-json tests/fixtures/releases.json --discussions-json tests/fixtures/discussions.json
[ "$($A sql "SELECT count(*) AS n FROM item_comment" | sed -n 3p | tr -d ' ')" = "7" ] || fail "7 comments expected (the one on an unknown item is skipped)"
[ "$($A next -n 10)" = "1 2 3 5" ] || fail "next must list unread issues and leave PRs out"
$A apply tests/fixtures/batch-ok.tsv
[ "$(count)" = "3" ] || fail "valid batch should give 3 analyses"

BEFORE=$(count)
if $A apply tests/fixtures/batch-bad.tsv 2> "$FI_HOME/bad.err"; then fail "bad batch was accepted"; fi
for msg in "single-valued" "unknown facet" "not in the taxonomy" "not in the database"; do
  grep -q "$msg" "$FI_HOME/bad.err" || fail "expected error text: $msg"
done
[ "$(count)" = "$BEFORE" ] || fail "a rejected batch must not change the database"

# register batches (.yaml): validated whole, atomic; a known-error needs a workaround
reg() { $A sql "SELECT count(*) AS n FROM register" | sed -n 3p | tr -d ' '; }
if $A apply tests/fixtures/register-bad.yaml 2> "$FI_HOME/regbad.err"; then fail "bad register batch was accepted"; fi
for msg in "id must be lowercase" "type must be one of" "not in the database" "unknown facet" "not in the taxonomy" "needs a workaround" "single-valued"; do
  grep -q "$msg" "$FI_HOME/regbad.err" || fail "expected register error text: $msg"
done
[ "$(reg)" = "0" ] || fail "a rejected register batch changed the database"
$A apply tests/fixtures/register-ok.yaml
[ "$(reg)" = "3" ] || fail "3 register entries expected"
STATUS_OUT="$($A status)"   # capture first (see lessons: `| grep -q` closes the pipe early)
grep -q "register: problem=1, request=1, risk=1" <<<"$STATUS_OUT" || fail "status must summarise the register"
$A status | head -1 >/dev/null || fail "a closed pipe must not break a read-only command"
if $A sql "INSERT INTO tag VALUES (1, 'kind', 'not-a-kind')" 2>/dev/null; then fail "database accepted a tag outside the taxonomy"; fi

# the file and the database must not silently disagree: `check` warns, `apply` refuses with a readable message
grep -v "^      environment:" tests/fixtures/taxonomy.yaml > "$FI_HOME/tax-drift.yaml"
DRIFT_OUT="$(FI_TAXONOMY="$FI_HOME/tax-drift.yaml" $A check || true)"   # capture first: `| grep -q` closes the pipe early and pipefail turns that into a failure
grep -q "taxonomy drift: value cause:environment is in database only" <<<"$DRIFT_OUT" || fail "drift not reported by check"
if FI_TAXONOMY="$FI_HOME/tax-drift.yaml" $A apply tests/fixtures/batch-ok.tsv 2> "$FI_HOME/drift.err"; then fail "apply must refuse when taxonomy.yaml and the database disagree"; fi
grep -q "disagree" "$FI_HOME/drift.err" || fail "expected a readable drift message"
# .sql batches: one transaction; a failing statement must leave everything untouched
pot() { $A sql "SELECT value FROM tag WHERE item_n = $1 AND facet = 'pr_potential'" | sed -n 3p | tr -d ' '; }
[ "$(pot 3)" = "code-fix" ] || fail "fixture precondition"
if $A apply tests/fixtures/retag-bad.sql 2> "$FI_HOME/sqlbad.err"; then fail "bad .sql batch was accepted"; fi
grep -q "nothing was written" "$FI_HOME/sqlbad.err" || fail "expected a rejection message for the .sql batch"
[ "$(pot 3)" = "code-fix" ] || fail "a rejected .sql batch changed the database"
$A apply tests/fixtures/retag-ok.sql
[ "$(pot 1)" = "resolved" ] && [ "$(pot 2)" = "wontfix" ] || fail ".sql batch was not applied"
$A check || true
$A status
$A render --out "$FI_HOME/out1"
$A render --out "$FI_HOME/out2"
diff -r "$FI_HOME/out1" "$FI_HOME/out2" >/dev/null || fail "render is not deterministic"
O="$FI_HOME/out1"
for f in index.md coverage.md health.md triage.md register.md register/docs-gap.md register/one-person-carries-it.md by/cause/doc-gap.md provenance.md; do test -f "$O/$f" || fail "missing page $f"; done
! grep -rq "built-in method" "$O" || fail "a template read a dict method instead of a column"
grep -q "Users cannot find how to uninstall" "$O/register.md" || fail "register entry not rendered"
grep -q "Known error" "$O/register/docs-gap.md" || fail "a known-error must show its workaround"
# health: every figure below was calculated by hand from the fixtures
grep -q "| 2021 | 2 | 1 | 67% |" "$O/health.md" || fail "maintainer share of comments (2021)"
grep -q "| 2022 | 2 | 1 | 67% |" "$O/health.md" || fail "maintainer share of comments (2022; includes the review comment)"
grep -q "| 2021 | 4 | 3 | 1 | 25% |" "$O/health.md" || fail "median days to first response / no response (2021; the bot comment must not count)"
grep -q "| 2021 | 1 | 1 | 1 | 100% |" "$O/health.md" || fail "pull request closure ratio (2021)"
grep -q "| 2021 | 2 | 1 | 1 |" "$O/health.md" || fail "contributor absence factor (2021)"
grep -q "| 2021 | 1 |$" "$O/health.md" || fail "release count must exclude pre-releases"
grep -q "| 2022 | 1 | 1 |" "$O/health.md" || fail "discussions with no reply (2022)"
grep -q "uninstall" "$O/by/cause/doc-gap.md" || fail "facet page lacks item text"
HASH=$(grep -o 'commit `[0-9a-z]*`' "$O/provenance.md" | grep -o '[0-9a-z]\{12\}')
[ "$(grep -rl "$HASH" "$O" | wc -l)" = "1" ] || fail "the database commit stamp must appear on exactly one page"

$A export --dir "$FI_HOME/e1"; $A export --dir "$FI_HOME/e2"
diff -r "$FI_HOME/e1" "$FI_HOME/e2" >/dev/null || fail "export is not deterministic"
python tests/check_mkdocs.py
[ ! -d .doltcfg ] || fail "server state leaked into the repository working directory"
# undo: dolt_reset removes the last commit (documented in playbook/09-operate.md)
$A sql "SELECT dolt_reset('--hard', 'HEAD~1')" >/dev/null
[ "$(pot 1)" = "docs-fix" ] || fail "dolt_reset did not undo the last commit (the .sql re-tag)"
[ "$(reg)" = "3" ] || fail "dolt_reset must not undo earlier commits"
# an existing database (baseline schema + a problem) must upgrade in place with its data intact
MAIN_DB="$FI_DATABASE"; export FI_DATABASE="fi_mig_$$_$RANDOM"
FI_MIGRATE_MAX=0 $A db init >/dev/null
$A sql "INSERT INTO item VALUES (1, 'old item', false, 'OPEN', '2021-01-01', NULL, 'a', 0, '')" >/dev/null
$A sql "INSERT INTO problem VALUES ('old-problem', 'An old problem', 'Written before the register existed.', 'open')" >/dev/null
$A sql "INSERT INTO problem_item VALUES ('old-problem', 1)" --commit "test: data written under the old schema" >/dev/null
MIG_OUT="$($A db init)"
grep -q "migrated: 001-register" <<<"$MIG_OUT" || fail "the migration did not run"
[ "$($A sql "SELECT type FROM register WHERE id = 'old-problem'" | sed -n 3p | tr -d ' ')" = "problem" ] || fail "old problem was not carried into the register"
[ "$($A sql "SELECT count(*) AS n FROM register_item WHERE register_id = 'old-problem'" | sed -n 3p | tr -d ' ')" = "1" ] || fail "old evidence link was lost"
if $A sql "SELECT 1 FROM problem" >/dev/null 2>&1; then fail "the old problem table should be gone"; fi
[ "$($A sql "SELECT max(version) AS v FROM schema_migration" | sed -n 3p | tr -d ' ')" = "2" ] || fail "migrations not recorded"
export FI_DATABASE="$MAIN_DB"
$A sql "SELECT 1" >/dev/null   # server still healthy
echo "ALL TESTS PASSED"
