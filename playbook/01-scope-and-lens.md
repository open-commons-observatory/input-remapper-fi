# 1. Scope and lens

Write down, before reading anything: the decision the FI repository must support, the questions it must answer, what is
**out** of scope, and how deeply items will be read. Put it in `SCOPE.md` in your FI repository and link it from the README.

A **[lens](lenses.md)** is the purpose you apply to the corpus. Pick the closest one (landscape, exhaustive dataset,
support burden, contribution, prior art, ...). The lens decides which facets you need, so pick it *before* designing the
vocabulary: adding a facet after tagging means re-reading records.

Decide the **depth budget** per item type: `title` (list only), `thread` (opening post plus maintainer replies),
`full` (whole thread), `source` (checked against code or docs). Depth is stored per item and shown on the coverage page.

State the known limits at the start (single maintainer, young project, one analyst) so they are visible at the end.
