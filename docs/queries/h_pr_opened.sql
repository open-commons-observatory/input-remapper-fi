SELECT CAST(extract(year FROM created) AS int) AS year, count(*) AS opened FROM item WHERE is_pr GROUP BY 1 ORDER BY 1;
