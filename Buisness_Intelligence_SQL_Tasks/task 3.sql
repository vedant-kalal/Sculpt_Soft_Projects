-- Identify most sold products in the last 3 months.

select p.name as product_name, sum(oi.quantity) as total_units_sold
from order_items oi
join orders o on o.order_id=oi.order_id
join products p on p.product_id=oi.product_id
where o.order_date >= CURDATE() - INTERVAL 3 MONTH
group by p.name
order by total_units_sold desc;


