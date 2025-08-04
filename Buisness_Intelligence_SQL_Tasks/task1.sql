-- List the top 10 customers by total spend.
select c.customer_id,c.name,sum(o.total_amount) as total_spent
from customers c 
join orders o on c.customer_id=o.customer_id
group by c.customer_id,c.name
order by total_spent desc
limit 10;
