# Lenses

A lens is the purpose you apply to a corpus. Pick the closest, adjust, and decide the facets from the **union** of your lenses
*before* tagging. `[ok]` = supported by the current schema, `[planned]` = needs a schema extension (see [migration](migration-from-v1.md)).

| Lens | Question it answers | Extra facets or work | Deliverable | Support |
|---|---|---|---|---|
| **Landscape** | What goes wrong here, how often, who answers? Hours, not days. | coarse `kind`, `outcome` from titles and opening posts; do not present as exhaustive | statistics page | [ok] |
| **Dataset** | Everything read, tagged, summarised, depth recorded. | the full vocabulary | the database; all reports generated from it | [ok] |
| **Contribution** | Which problems can a pull request close? | `pr_potential`; problem registry | triage queue, problem pages, PRs | [ok] |
| **Support burden** | Where do docs and support time go? | `doc-gap`, `spam`, counts per year | docs-gap list, repeated questions | [ok] |
| **Prior art** | What did a predecessor learn that a successor must not repeat? | cause, outcome, constraint notes | a findings document per problem class | [ok] for issues; commit reading [planned] |
| **Rule catalogue** | Which constraints does the project enforce or violate, verified against a newer version? | a `constraint` facet; full reads; `source` depth | validator and guard inputs | [planned] |
| **Successor comparison** | Which old findings still hold in the successor or fork? | two corpora, one vocabulary, a status facet | side-by-side table | [planned] (schema is single-corpus) |
| **Design history** | Why is it built this way? | commits in date order; decision-bearing commits | timeline | [planned] (commit analysis) |
| **Detector input** | How are failures detected; where does measurement mislead? | read for validity, false positives and negatives | notes per detector | [ok] |
| **Refresh** | What is new since the last run? | none | updated pages | [ok] (`fi acquire`, then `fi next`) |

`pr_potential` values: `code-fix`, `docs-fix`, `needs-design`, `upstream-dep`, `close-duplicate`, `wontfix`, `unknown`. Assess with
`conf:inferred` until a maintainer confirms.
