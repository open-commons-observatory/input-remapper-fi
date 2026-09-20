# Instructions for AI agents (and for humans): this repository is its own manual

This file is the entry point. It applies to the template (`foss-insights`) and to every FI repository created from it (`<project>-fi`).

## 1. The repository is the working context

This repository was written by an AI, for the next AI. **At the start of every session, read it in full, in this order, before doing any work:**

1. `README.md`, then `ROADMAP.md` (what is planned, staged and open).
2. `playbook/README.md`, `playbook/methodology.md`, `playbook/principles.md`, `playbook/lessons.md` (every lesson: each one cost time) and `playbook/agent-manual.md` (environment, procedures, checks).
3. `decisions/`: **every** decision record, in order. They say what was chosen, what was rejected and why.
4. `fi.yaml`, `taxonomy.yaml`, `db/migrations/`, and `python tools/fi.py --help`.
5. In an FI repository also: `SCOPE.md`, the list of `batches/`, and the output of `python tools/fi.py status`.

Do not skim. Earlier sessions lost time on things that were already written down. If something you need is not written down, that is a gap to fix (rule 2), not a reason to guess.

## 2. Update it as you go

A chat is not a record; the repository is. Whatever a session learns goes into the repository **in the same commit as the change that taught it**:

| What happened | Where it goes |
|---|---|
| a decision (a choice between options) | a new decision record in `decisions/` |
| a mistake, trap or surprise | a new numbered entry in `playbook/lessons.md` |
| a procedure changed or was found to be wrong | the matching `playbook/` document |
| a task started, finished or newly discovered | `ROADMAP.md` |
| a fact turned out wrong | fix it visibly ("Corrected: ...", with the date), never silently |

## 3. Decisions are additive

- Decision records are **append-only**. Never delete one and never change what an accepted one decided.
- To change your mind, write a **new** record with the next number, and add a single line to the old one: `Superseded (in part) by ADR-00NN`.
- Number sequentially: the next number is the highest existing one plus one. Lessons are appended and never renumbered.
- Every record states the options considered and why the others were rejected, and what is known to be unverified.

## 4. Session checklists

**Start:** read the repository (rule 1); run the state check in `playbook/agent-manual.md`; report any difference between the repository's claims and reality before working.
**End:** everything learned is in the repository (rule 2); `ROADMAP.md` matches reality; tests pass; nothing is pushed that was not verified; report done / not done / next.

## 5. Working agreement (short; details in `playbook/agent-manual.md`)

- **Secrets:** the GitHub token is provided by the user each session and lives only in the environment. Never write it to a file, a commit, a log or a record. Scan staged content before every commit.
- **Prove, do not assert.** CI green, live pages checked, numbers compared with the database, important figures recomputed by an independent path. Say plainly what was not done or not read.
- **Gate every push** on the tests and on real exit statuses, never on a pipe through `tail` or `grep -q`.
- **Ask first** before anything public or hard to undo: opening pull requests upstream, deleting or archiving repositories, choosing a license, merging a release, changing branch protection.
- **Privacy and copyright:** store only who, where and when about comments, never their text; paraphrase what people wrote.
- Everything is done in the open: public repositories, public decisions.

## 6. Map

`playbook/` the method and this manual; `decisions/` decision records; `db/migrations/` the schema; `tools/` the `fi` command and page generator; `docs/` SQL, templates and page list; `tests/` the self-test; `.github/workflows/` CI. An FI repository adds `batches/`, `data/`, `docs/generated/`, `SCOPE.md`.
