-- 1581: Customer who visited but did not make any transactions
SELECT v.customer_id, COUNT(*) as count_no_trans
FROM Visits v
WHERE v.visit_id NOT IN (
    SELECT DISTINCT visit_id FROM Transactions
)
GROUP BY customer_id
;

