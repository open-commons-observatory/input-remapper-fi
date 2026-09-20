# 7. Register and changes

Items are evidence. A **register entry** is a conclusion drawn from evidence, and the register is the one list of everything worth acting on
([methodology](methodology.md)). Four types:

| Type | What it is | Example |
|---|---|---|
| `problem` | a root cause behind many items | the `uinput` module is not loaded, so injection fails |
| `request` | a capability that does not exist | a Qt user interface |
| `improvement` | refactoring, tests, docs, process | dependency injection, so tests get easier |
| `risk` | something that could hurt the project | the only maintainer has stepped back |

A problem with a workaround and no fix is a **known error**: status `known-error`, and the `workaround` field is required.

## Writing entries

Entries live in `batches/NNNN-<what>.yaml` (validated whole, applied atomically, one commit). Quote any text containing `: `.

```yaml
- id: di-testability
  type: improvement
  title: "Dependency injection for testability"
  summary: "Global state and utility classes make tests hard to write; a start was made in 2024 ..."
  status: in-progress            # open | known-error | in-progress | pr-planned | pr-open | closed | wontfix
  items: [853, 960, 964]         # evidence: every entry needs at least one item
  tags:
    change_type: [preventive]    # corrective | adaptive | perfective | preventive | additive
    quality: [maintainability]   # ISO/IEC 25010:2023
    dimension: [information-technology]
    value: [high]
    effort: [large]
    risk: [medium]
    conf: [stated]
```

```bash
python tools/fi.py apply batches/0019-register.yaml --dry-run
python tools/fi.py apply batches/0019-register.yaml
python tools/fi.py check          # warns about entries with no evidence, or with no value/effort tag
```

## From entry to pull request

1. **Verify against the current source** before proposing anything (read the docs and code, record the commit you checked). Old items are often already fixed.
2. **Classify the change** (`change_type`) and say what it risks (`risk`). Reactive changes (corrective, adaptive) are what users feel; proactive ones (preventive, perfective, additive) are what keep the project changeable.
3. **Prefer small pull requests, one per entry**, and name the entry and its evidence items in the description. Match the project's own rules (tests, linting) and check what maintainers said about how they review.
4. Set the status to `pr-planned`, then `pr-open`, then `closed`.

The rendered `register.md` also lists **actionable items not yet in any entry**; work that list down to empty.
