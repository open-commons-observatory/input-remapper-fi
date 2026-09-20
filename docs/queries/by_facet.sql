SELECT t.facet, t.value, count(*) AS n FROM tag t JOIN facet f ON f.name = t.facet WHERE f.page GROUP BY t.facet, t.value ORDER BY t.facet, n DESC, t.value;
