SELECT substr(commit_hash,1,12) AS hash, message, date::date AS date FROM dolt_log LIMIT 1;
