# ADR-0003: Renamed to `input-remapper-fi` (FOSS Insights)

Status: done (2026-09-20). Template decision: see `decisions/ADR-0003` in [foss-insights](https://github.com/open-commons-observatory/foss-insights).

The repository `input-remapper-oco-atlas` became `input-remapper-fi`; the tool is now `python tools/fi.py`, the config `fi.yaml`, the database `fi`.
Earlier decision records in this repository keep the names they were written with.

**Checked, not assumed:** the database cloned from GitHub under the new name matches the pre-rename push (1,099 items, 192 analyses, 1,662 tags, 5 problems,
head `803n75h0344d`) and `fi export` produced no CSV change; `fi db push` repaired the database's stored remote URL; git URLs of the old name redirect;
**the old GitHub Pages address returns 404 (no redirect)**, the new one is https://open-commons-observatory.github.io/input-remapper-fi/.
