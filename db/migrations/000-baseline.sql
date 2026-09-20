-- FOSS Insights core schema (Postgres dialect, runs on Doltgres). Each statement ends with ';' at end of line.
-- The vocabulary lives in tables so the database itself refuses a tag that is not in the taxonomy.
CREATE TABLE facet (
  name  text PRIMARY KEY,
  multi boolean NOT NULL,
  page  boolean NOT NULL DEFAULT false,
  doc   text NOT NULL
);
CREATE TABLE facet_value (
  facet text NOT NULL REFERENCES facet(name),
  value text NOT NULL,
  doc   text NOT NULL,
  PRIMARY KEY (facet, value)
);
-- Issues and pull requests of the analysed project.
CREATE TABLE item (
  n        int PRIMARY KEY,
  title    text NOT NULL,
  is_pr    boolean NOT NULL,
  state    text NOT NULL CHECK (state IN ('OPEN','CLOSED','MERGED')),
  created  date NOT NULL,
  closed   date,
  author   text NOT NULL,
  comments int NOT NULL CHECK (comments >= 0),
  labels   text NOT NULL DEFAULT ''
);
CREATE TABLE git_commit (
  sha       text PRIMARY KEY,
  subject   text NOT NULL,
  author    text NOT NULL,
  committed date NOT NULL
);
-- One row per item that has been read: how deeply, and what it says.
CREATE TABLE analysis (
  item_n  int PRIMARY KEY REFERENCES item(n),
  batch   text NOT NULL,
  depth   text NOT NULL CHECK (depth IN ('title','thread','full','source')),
  summary text NOT NULL CHECK (summary <> '')
);
CREATE TABLE tag (
  item_n int  NOT NULL REFERENCES analysis(item_n),
  facet  text NOT NULL,
  value  text NOT NULL,
  PRIMARY KEY (item_n, facet, value),
  FOREIGN KEY (facet, value) REFERENCES facet_value(facet, value)
);
-- Problem registry: recurring problems (many items -> one problem -> one fix).
CREATE TABLE problem (
  id      text PRIMARY KEY,
  title   text NOT NULL,
  summary text NOT NULL,
  status  text NOT NULL DEFAULT 'open' CHECK (status IN ('open','pr-planned','pr-open','closed','wontfix'))
);
CREATE TABLE problem_item (
  problem_id text NOT NULL REFERENCES problem(id),
  item_n     int  NOT NULL REFERENCES item(n),
  PRIMARY KEY (problem_id, item_n)
);
