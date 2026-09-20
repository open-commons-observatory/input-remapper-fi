# 7. Problems and pull requests

Items are symptoms; a **problem** is a recurring failure with one root cause and, usually, one fix. The registry has two tables:
`problem` (id, title, summary, status) and `problem_item` (which items belong to it). Statuses: `open`, `pr-planned`, `pr-open`,
`closed`, `wontfix`.

```bash
python tools/fi.py sql "INSERT INTO problem VALUES ('bt-autoload', 'Bluetooth devices are not autoloaded', 'udev fires before the device is ready ...', 'open')"
python tools/fi.py sql "INSERT INTO problem_item VALUES ('bt-autoload', 25), ('bt-autoload', 107), ('bt-autoload', 274)" --commit "registry: bt-autoload"
```

The rendered `problems.md` also lists **actionable items not yet assigned to a problem** (`pr_potential` of `code-fix` or
`docs-fix`): that list is your grouping backlog. Work it down to empty.

Then, per problem: verify the claim against the project's code or docs (depth `source`), check whether a fix already landed,
and open one PR that closes the group. Record the PR number in the problem summary and move the status to `pr-open`, then `closed`.
Prefer a PR per problem, not per item; say in the PR which items it closes.
