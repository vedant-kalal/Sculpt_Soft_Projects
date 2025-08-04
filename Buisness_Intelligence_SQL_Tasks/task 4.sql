-- Calculate the conversion rate (orders/site visits) if given a site_visits table.
SELECT 
COUNT(DISTINCT o.order_id) * 1.0 / COUNT(DISTINCT sv.visit_id) AS conversion_rate
FROM site_visits sv
LEFT JOIN orders o 
ON sv.customer_id = o.customer_id 
AND sv.visit_date = o.order_date;
