SELECT t.facet, t.value FROM tag t JOIN facet f ON f.name = t.facet WHERE f.page GROUP BY t.facet, t.value ORDER BY t.facet, t.value;
