SELECT facet, sum(CASE WHEN value = 'unknown' THEN 1 ELSE 0 END) AS unknown, count(*) AS total FROM tag GROUP BY facet HAVING sum(CASE WHEN value = 'unknown' THEN 1 ELSE 0 END) > 0 ORDER BY facet;
