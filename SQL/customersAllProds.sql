-- 1045: Customers who bought all Products
SELECT c1.customer_id
FROM (SELECT customer_id, COUNT(DISTINCT product_key) AS num FROM CUSTOMER GROUP BY customer_id) c1 
WHERE c1.num=(SELECT COUNT(DISTINCT product_key ) FROM PRODUCT) 
;
