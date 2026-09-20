SELECT ri.item_n AS n, i.title, i.state, a.summary FROM register_item ri JOIN item i ON i.n = ri.item_n LEFT JOIN analysis a ON a.item_n = ri.item_n WHERE ri.register_id = %(id)s ORDER BY ri.item_n;
