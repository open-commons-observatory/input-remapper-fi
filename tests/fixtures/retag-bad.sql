-- tests: the first statement is valid, the second breaks a constraint: nothing may be written
UPDATE tag SET value = 'wontfix' WHERE item_n = 3 AND facet = 'pr_potential';
UPDATE tag SET value = 'nonsense' WHERE item_n = 1 AND facet = 'pr_potential';
