-- 001: one register for everything worth acting on (ITIL 4 "continual improvement register").
-- Replaces the problems-only tables. Types: problem (root cause), request (new capability), improvement (refactoring, debt, docs, process), risk.
-- A problem with a workaround but no fix is a KNOWN ERROR (status known-error, workaround filled in).
CREATE TABLE register (
  id         text PRIMARY KEY,
  type       text NOT NULL CHECK (type IN ('problem','request','improvement','risk')),
  title      text NOT NULL,
  summary    text NOT NULL,
  status     text NOT NULL DEFAULT 'open' CHECK (status IN ('open','known-error','in-progress','pr-planned','pr-open','closed','wontfix')),
  workaround text
);
-- Evidence: the items (issues, PRs) that show the entry is real.
CREATE TABLE register_item (
  register_id text NOT NULL REFERENCES register(id),
  item_n      int  NOT NULL REFERENCES item(n),
  PRIMARY KEY (register_id, item_n)
);
-- Classification uses the same vocabulary as item tags (facet:value), so it is enforced the same way.
CREATE TABLE register_tag (
  register_id text NOT NULL REFERENCES register(id),
  facet       text NOT NULL,
  value       text NOT NULL,
  PRIMARY KEY (register_id, facet, value),
  FOREIGN KEY (facet, value) REFERENCES facet_value(facet, value)
);
INSERT INTO register SELECT id, 'problem', title, summary, status, NULL FROM problem;
INSERT INTO register_item SELECT problem_id, item_n FROM problem_item;
DROP TABLE problem_item;
DROP TABLE problem;
