# Finish the move to dependency injection so tests become easier to write

`improvement` · status `in-progress` · 4 evidence items · [Back to the register](../register.md)

In #853 the maintainer says that, looking back, he wishes he had applied the dependency-injection pattern everywhere because it would have made tests easier to write; the tool is stable thanks to its high test coverage. He started in autumn 2024: PR #960 (merged) introduced wrapper classes for path and user handling and migrations that can be replaced in tests, and added TODO comments wherever a global object should be injected instead; PR #964 (merged) continued it. He noted that injecting the macro parser is hard because mapping objects have to be serialised. PR #1068 (custom groups, still open since February 2025) lists dependency injection for groups as an unfinished item. So the direction is accepted and partly done; what is missing is someone to carry it on in reviewable steps.

| Facet | Values |
|---|---|
| change_type | preventive |
| conf | stated |
| dimension | information-technology |
| effort | large |
| quality | maintainability |
| risk | medium |
| value | high |

## Evidence

| Item | State | Title | Summary |
|---|---|---|---|
| [#853](https://github.com/sezanzeb/input-remapper/issues/853) | OPEN | State of Maintenance |  |
| [#960](https://github.com/sezanzeb/input-remapper/issues/960) | MERGED | Improved test setup |  |
| [#964](https://github.com/sezanzeb/input-remapper/issues/964) | MERGED | Dependency injection |  |
| [#1068](https://github.com/sezanzeb/input-remapper/issues/1068) | OPEN | Custom groups |  |
