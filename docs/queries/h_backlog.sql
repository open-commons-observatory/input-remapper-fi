SELECT CASE WHEN is_pr THEN 'pull requests' ELSE 'issues' END AS kind, count(*) AS open_items, min(created) AS oldest FROM item WHERE state = 'OPEN' GROUP BY is_pr ORDER BY is_pr;
