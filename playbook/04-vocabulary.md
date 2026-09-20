# 4. Vocabulary

`taxonomy.yaml` is the data dictionary: facets, and for each facet its allowed values with a one-line definition. `atlas db init`
(and `atlas db init` again after edits) loads it into the `facet` and `facet_value` tables. **The database rejects any tag that is
not in the vocabulary** (a foreign key), so a typo cannot be stored.

- `multi: false` facets take one value per item (`kind`, `outcome`, `conf`); `multi: true` facets take several (`cause`, `impact`).
- `page: true` renders one page per used value under `by/<facet>/<value>.md`.
- Every facet needs an `unknown` value where "not established" is a legitimate answer. Count them: `atlas check` warns when a
  quarter or more of a facet's tags are `unknown`.
- Quote values YAML would read as booleans (`yes`, `no`, `on`, `off`); `atlas` refuses non-string values.

Design from the [lens](lenses.md), sample about 100 titles, draft the facets, then read the first 30-50 items and revise **before**
the main loop. Renaming or removing a value that tags already use is refused until you retag those items.

The starter vocabulary is generic (`kind`, `outcome`, `cause`, `impact`, `conf`, `pr_potential`). Add your project's own facets
(for example the layer of the system, the device, the operating system) beside them.
