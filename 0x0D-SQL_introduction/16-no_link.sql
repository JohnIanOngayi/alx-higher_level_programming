-- Script that lists records of table where certain attribute is not NULL
SELECT score, name
FROM second_table
WHERE name IS NOT null
ORDER BY score DESC;
