# 10. Project health

`fi acquire` also collects who commented where and when (never the text), releases, and GitHub Discussions. `health.md` turns that into the
[CHAOSS](https://chaoss.community) starter metrics: comments per year (maintainers versus everyone else), median days to first response and the share of issues that never
got one, pull-request closure ratio, contributor absence factor, releases per year, discussions without a reply, and today's open backlog.

Use it to ask project-level questions that no single issue answers: is the maintainer still responsive, is the backlog growing, does one person carry the project.
Then record the answer as a **risk** entry in the register, citing the evidence items (an announcement, a comment where the maintainer explains) beside the numbers.
The metrics describe activity, not intent: see the limits in [methodology](methodology.md#limits-worth-stating).

Bots are excluded from every response number. Maintainers are the logins in `fi.yaml` (`source.maintainers`). GitHub Discussions need `GITHUB_TOKEN` (GraphQL);
without it that part is skipped and said so.
