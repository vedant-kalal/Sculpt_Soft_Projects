select p.category,count(p.category) as sellings_per_category,
sum(oi.quantity * oi.price) as total_revenue
from order_items oi
join products p on oi.product_id = p.product_id
group by p.category
order by total_revenue desc;
