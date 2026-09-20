-- Re-tag: pr_potential 'unknown' -> 'resolved' where no change to the project is needed.
-- Evidence (2026-09-20): of 89 items tagged pr_potential:unknown, 70 are CLOSED with outcome 'fixed' (61) or 'workaround' (9).
-- 'unknown' on those meant "already resolved", not "not assessed"; the vocabulary had no value for that, so 'resolved' was added.
-- Deliberately NOT touched (still 'unknown', they need a real second look): 19 items that are open, unresolved, environment-side
-- or tagged outcome:fixed while still OPEN upstream (198, 220, 258).
UPDATE tag SET value = 'resolved' WHERE facet = 'pr_potential' AND value = 'unknown' AND item_n IN (1, 2, 4, 6, 7, 8, 10, 12, 13, 19, 23, 25, 28, 30, 33, 35, 36, 37, 40, 41, 44, 46, 47, 49, 53, 58, 59, 61, 65, 67, 71, 73, 74, 76, 78, 79, 93, 98, 99, 103, 107, 109, 120, 125, 142, 150, 170, 171, 181, 183, 185, 186, 197, 204, 211, 213, 218, 221, 225, 229, 231, 240, 247, 248, 253, 266, 276, 278, 281, 283);
