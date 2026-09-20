# 8. Publish

```bash
python tools/fi.py render        # docs/generated/*.md and mkdocs.yml, from SQL files + Jinja templates
python tools/fi.py export        # data/*.csv, primary-key sorted, reviewable in a pull request
python tools/fi.py db push       # the database itself, into refs/dolt/data
git add -A && git commit -m "regenerate" && git push
```

- **What is rendered** is described in `docs/pages.yaml`: template, SQL queries (`docs/queries/`), output path. A page with
  `for_each` renders once per row of a query (one page per facet value, one per problem). Edit templates in `docs/templates/`.
- **Generated Markdown renders on GitHub as it is** (tables and Mermaid included), so a local render plus push is a complete
  publishing path. CI additionally builds an HTML site with [Zensical](https://zensical.org) and deploys GitHub Pages
  (enable Pages, source: GitHub Actions).
- **Order matters.** Pushing the database does not trigger workflows (it goes to a hidden ref). Push the database first, then push
  the regenerated files; CI clones the database and fails if the committed pages or CSV differ from a fresh render.
- **Provenance:** the database commit is stamped on exactly one page (`provenance.md`). Stamping every page would rewrite every
  file on every data change.
