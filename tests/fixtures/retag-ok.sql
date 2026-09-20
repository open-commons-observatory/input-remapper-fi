-- tests: a valid bulk re-tag
UPDATE tag SET value = 'resolved' WHERE item_n = 1 AND facet = 'pr_potential';
UPDATE tag SET value = 'wontfix' WHERE item_n = 2 AND facet = 'pr_potential';
