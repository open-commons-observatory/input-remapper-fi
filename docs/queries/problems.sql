SELECT p.id, p.title, p.status, (SELECT count(*) FROM problem_item pi WHERE pi.problem_id = p.id) AS items FROM problem p ORDER BY p.status, p.id;
