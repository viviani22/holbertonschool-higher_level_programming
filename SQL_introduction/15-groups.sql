-- Lists the number of records with the same score in table
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
