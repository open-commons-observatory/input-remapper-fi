SELECT pi.item_n AS n, i.title, i.state, a.summary FROM problem_item pi JOIN item i ON i.n = pi.item_n LEFT JOIN analysis a ON a.item_n = pi.item_n WHERE pi.problem_id = %(id)s ORDER BY pi.item_n;
