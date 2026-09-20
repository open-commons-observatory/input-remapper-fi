SELECT facet, string_agg(value, ', ' ORDER BY value) AS vals FROM register_tag WHERE register_id = %(id)s GROUP BY facet ORDER BY facet;
