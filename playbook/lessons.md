# Lessons from building v2

Lessons about the method itself are in [lessons-v1.md](lessons-v1.md) (66 of them, written for markdown records; the ones about
tagging, reading and honesty still hold). These are new, found while rebuilding on a database.

1. **Check a dependency's health before adopting it.** Evidence's open-source template became a hosted product (login required); Material for
   MkDocs reaches end of life on 2026-11-05 and MkDocs has been unmaintained since 2024. Look at licence, last release, last commit and the
   README's own status note, not just stars.
2. **Keep the product Markdown, make the HTML layer swappable.** Generated Markdown renders on GitHub as it is; a static-site generator
   is optional and replaceable.
3. **In Jinja, `row.items` on a dict is the dict method.** Columns named `items`, `keys`, `values`, `get`... silently print a memory
   address. Rows are wrapped in namespaces and a test greps for it.
4. **Doltgres writes `.doltcfg/` into its working directory.** Start it from a directory outside the repo; `git add -A` will otherwise
   commit the server's auth databases.
5. **A validator that ignores what it does not understand reports success.** Two `conf=stated` typos passed "all records valid".
   Constraints in the database reject them.
6. **Do not stamp every generated file with the data version.** One data change then rewrites every file. Stamp one provenance page.
7. **Pushing the database does not trigger CI** (hidden ref). Push the database, then the regenerated files; CI verifies they match.
8. **Look up GitHub Action versions.** Memory was two major versions behind.
9. **Tests need a private database.** A shared server that already holds data breaks tests that assume an empty one.
10. **`pkill -f` / `pgrep -f` match their own shell** when the pattern is in the command line. Use `pkill -x name`.
11. **Never encode a path twice** when calling the Contents API (a file was created with a literal `%20` in its name).
12. **YAML turns `yes`, `no`, `on`, `off` into booleans.** A vocabulary value called `no` becomes `False`; `atlas` refuses non-string values.
13. **A fork needs a public, fork-enabled source.** A private repo with forking disabled cannot be forked, and a fork of a private repo
    cannot be a public template; import the history into a fresh repo instead.
14. **Measure before believing a bug report.** A reported 45-80 s push to GitHub did not reproduce (5-8 s) on current versions.
15. **Claims about compatibility need a build.** "Reads mkdocs.yml" was true for Zensical; it took one build to know.
16. **GitHub contexts are scoped.** `runner.*` and `steps.*` do not exist in job-level `env:`; the workflow is rejected as a whole and shows up as a
    failed run named after the file path, with no jobs. Set such values in a step (`echo "X=$RUNNER_TEMP/x" >> "$GITHUB_ENV"`). Local tests cannot
    catch this; only a real run does.
17. **Quote every user-supplied value you write into YAML.** `site_name: proj: title` is a syntax error; use `| tojson`. The default title had no colon, so
    only a real project exposed it: test with hostile input (colons, quotes, `#`), not just the happy path.
18. **Generated repos have no upgrade path unless you write one.** Document how an instance takes template fixes ([operate](09-operate.md)) and use it for
    real on the first instance.
19. **Do not nest heredocs with the same terminator, and do not `pkill -f` a pattern that appears in your own command line.** Both hang or kill the shell.
    Put the inner script in its own file.
20. **Doltgres does not support `ILIKE` yet** (it answers "ILIKE is not yet supported"). Use `lower(col) LIKE '%term%'`. Keyword searches over summaries are a good way to find
    clusters, but read the hits: a search for "focus" found the real per-app-switching cluster (7 items) plus four unrelated items.
21. **A match in a file is not the feature existing.** When verifying an old request against current source, grep for file names first, then read the matching lines
    (`uninstall` and `focus` matched things that had nothing to do with the request). Record the upstream commit and date you verified against.
22. **Group before you plan PRs, and prune before you group.** Checking 2021-era "docs-fix" items against current docs removed four of them (already covered) before any PR was written.
23. **A push you did not check did not happen.** `atlas db push ... | tail -1 && git push` printed a credential hint, the chain continued, and GitHub kept a stale database.
    Never pipe a gating command through `tail`; check its exit status. The server needs `GITHUB_TOKEN` at *start*, not at call time.
