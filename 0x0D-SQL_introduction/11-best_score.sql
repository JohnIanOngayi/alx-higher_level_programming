-- Script that lists records above a certani value
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
