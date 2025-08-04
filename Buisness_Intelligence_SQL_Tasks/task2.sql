-- Generate a report of daily revenue and order count for the last 30 days.

select order_date, sum(total_amount) as daily_revenue, count(order_id) as no_of_orders
from orders
where order_date >= CURDATE() - INTERVAL 30  DAY
group by order_date
ORDER BY order_date;