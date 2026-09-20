SELECT CAST(extract(year FROM published) AS int) AS year, count(*) AS releases FROM project_release WHERE NOT prerelease GROUP BY 1 ORDER BY 1;
