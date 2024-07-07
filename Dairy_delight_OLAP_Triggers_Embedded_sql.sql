use Dairy_Model_1;

-- trigger 1 
-- giving reward to the person who is ordering again with an amount of rupees 200 to their wallet
drop trigger if exists cust_reward;
create trigger cust_reward
before insert on orders 
for each row 
update customer SET wallet_balance=wallet_balance+200 WHERE customer_id=NEW.customer_id;

-- showing customer 28, waller balance before adding  his new order in the dataset
select wallet_balance from customer where customer.customer_id = 28; 
-- inserting in orders
insert into Orders (amount,delivery_date,time_stamps,customer_id) values (5420,"Mar 10, 2022","8:29 AM",28);
-- showing wallet balance after the new order got added into the dataset
select wallet_balance from customer where customer. customer_id = 28;
alter table orders auto_increment = 101;
 delete FROM orders where order_id >101;
-- update customer SET wallet_balance = wallet_balance -400 where customer_id = 28;

-- trigger 2
-- giving discount to the person who has paid through UPI 
drop trigger if exists give_discount;
create trigger give_discount
before insert on invoice
for each row
update orders SET orders.amount = orders.amount - 100 Where NEW.order_id = orders.order_id;

-- entering the order 101
insert into orders (amount,delivery_date,time_stamps,customer_id) values (7880,"Mar 10, 2022","10:22 PM",41);
-- showing the order amount before the payment is made
select amount from orders where order_id = 101;
-- inserting the invoice 
insert into invoice values ("UPI","vitae@yahoo.net",101);
-- once the amount is added, we can see a measurable change in the amount section in the orders table

alter table orders auto_increment = 101;
delete FROM orders where order_id >101;
delete from invoice where order_id >= 101;


-- embeded_queries
-- embeded query 1
select count(*) as
orders_givendate_by_car,delivery_date from 
Orders where customer_id in 
(select customer_id FROM Delivery_Boy where vehicle_type="Car")
group by delivery_date
order by orders_givendate_by_car;

-- embeded query 2
select customer_name,boy_name,vehicle_type from
Customer c join Delivery_boy d on
c.Delivery_ID=d.Delivery_ID where 
age>(
select avg(age) from customer)
and wallet_balance>8000;


-- OLAP Queries
-- olap query 1
select customer_name,delivery_date,sum(amount) 
from customer natural join orders 
GROUP BY delivery_date, customer_name with rollup;

-- olap query 2
select mode_of_pay,delivery_date,sum(amount)
from invoice natural join orders
group by mode_of_pay, delivery_date with rollup; 

-- olap query 3
SELECT i.mode_of_pay,
SUM(CASE WHEN c.age < 18 THEN o.amount ELSE 0 END) as '< 18',
SUM(CASE WHEN c.age BETWEEN 18 AND 30 THEN o.amount ELSE 0 END) as '18-30',
SUM(CASE WHEN c.age BETWEEN 31 AND 50 THEN o.amount ELSE 0 END) as '31-50',
SUM(CASE WHEN c.age > 50 THEN o.amount ELSE 0 END) as '> 50'
FROM orders o
JOIN invoice i ON o.order_id = i.order_id
JOIN customer c ON o.customer_id = c.customer_id
GROUP BY i.mode_of_pay; 

-- olap query 4
SELECT SUM(amount) as total_sales
FROM orders o
JOIN invoice i ON o.order_id = i.order_id
JOIN customer c ON o.customer_id = c.customer_id
WHERE  i.mode_of_pay = 'UPI' AND c.age > 18 AND c.Gender = "Male";