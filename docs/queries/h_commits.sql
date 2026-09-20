SELECT CAST(extract(year FROM committed) AS int) AS year, author, count(*) AS n FROM git_commit GROUP BY 1, 2 ORDER BY 1, n DESC, author;
