-- Lists all records in the second_table table with a score >= 10,
-- ascending oeder
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
