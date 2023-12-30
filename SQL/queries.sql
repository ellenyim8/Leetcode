--1211: Queries quality and percentage
-- quality: avg of ratio between query rating and its position
-- poor query percentage: percentage of all queries with rating < 3 

SELECT query_name, ROUND((SUM(rating / position ) / COUNT(query_name)), 2) AS quality, ROUND(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100, 2) AS poor_query_percentage
FROM Queries 
GROUP BY query_name
;
