use Dairy_Model_1;

select customer_name,delivery_date,sum(amount) from customer natural join orders
GROUP BY delivery_date, customer_name with rollup;

select mode_of_pay,delivery_date,sum(amount) from invoice natural join orders  group by mode_of_pay,delivery_date with rollup;

select customer_name,delivery_date,sum(amount) from customer natural join orders
GROUP BY delivery_date, customer_name with rollup;