SELECT CAST(extract(year FROM created) AS int) AS year, count(*) AS discussions, sum(CASE WHEN comments = 0 THEN 1 ELSE 0 END) AS no_reply FROM discussion GROUP BY 1 ORDER BY 1;
