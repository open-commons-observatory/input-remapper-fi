# ADR-0002: The name `oco-atlas`, and rewriting the playbook as a template

Status: accepted (2026-09-20).

## Name
"Prior art" is a patent-law term (everything public before a date that bears on novelty). It fits one use of the method (mining a
predecessor before building a successor) and mislabels the others (triaging a live backlog). "Playbook" undersells a repo that is now
method + schema + tool + CI. Considered: Atlas, Problem Atlas, Issue Atlas, Evidence Atlas, Survey ("survey" reads as questionnaire),
Strata/Dig, Codebook. Chosen: **oco-atlas** (Open Commons Observatory Atlas). Convention: template `oco-atlas`, each analysis
`<project>-oco-atlas`. Old purposes ("prior art", "contribution") became [lenses](../playbook/lenses.md).

## Fork or fresh repo
Forking `sync-dot-mesh/prior-art-playbook` was impossible: it is private and forking is disabled, and a fork of a private repo would stay
private and could not be a public template. Chosen: a new public repo with the full history imported (scanned first: 17 commits,
0 secret-pattern hits, no analysis data embedded), tagged `v1-markdown-records` at the import point.

## Rewrite scope
Kept: the tagging method, batch format, and principles (revised). Replaced by tooling: bootstrap, indexes, checkpoint file, replay.
New: schema with constraints, `atlas` CLI, SQL + Jinja page generator, two workflows, a self-test. Deferred, on purpose: commit analysis,
multiple corpora, private-repo CI. Stack decisions are in ADR-0001.

## Defects found while building (all fixed, all covered by `tests/run.sh`)
A Jinja attribute lookup that returned a dict method instead of a column; test isolation on a shared server; server state written
into the working tree. See [lessons](../playbook/lessons.md).
