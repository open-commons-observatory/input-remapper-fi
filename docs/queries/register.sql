SELECT r.id, r.type, r.title, r.status,
  (SELECT count(*) FROM register_item ri WHERE ri.register_id = r.id) AS n_items,
  COALESCE((SELECT min(t.value) FROM register_tag t WHERE t.register_id = r.id AND t.facet = 'value'), '-') AS value,
  COALESCE((SELECT min(t.value) FROM register_tag t WHERE t.register_id = r.id AND t.facet = 'effort'), '-') AS effort,
  COALESCE((SELECT min(t.value) FROM register_tag t WHERE t.register_id = r.id AND t.facet = 'risk'), '-') AS risk,
  COALESCE((SELECT string_agg(t.value, ', ' ORDER BY t.value) FROM register_tag t WHERE t.register_id = r.id AND t.facet = 'change_type'), '-') AS change_type
FROM register r ORDER BY r.type, r.status, r.id;
