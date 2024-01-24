DROP TABLE IF EXISTS experiment;
DROP TABLE IF EXISTS reagent;


CREATE TABLE experiment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE reagent (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  reagent_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);