-- 002: activity data for project-health metrics (CHAOSS). Only who, where and when are stored, never the text of a comment.
CREATE TABLE maintainer (
  login text PRIMARY KEY
);
CREATE TABLE item_comment (
  id        bigint PRIMARY KEY,
  item_n    int     NOT NULL REFERENCES item(n),
  author    text    NOT NULL,
  created   date    NOT NULL,
  is_review boolean NOT NULL
);
CREATE TABLE project_release (
  tag        text PRIMARY KEY,
  published  date NOT NULL,
  prerelease boolean NOT NULL DEFAULT false
);
-- GitHub Discussions are a support channel of their own (they are not in the issues API).
CREATE TABLE discussion (
  n        int PRIMARY KEY,
  title    text NOT NULL,
  author   text NOT NULL,
  created  date NOT NULL,
  comments int  NOT NULL CHECK (comments >= 0),
  answered boolean NOT NULL DEFAULT false
);
