#Display customer_id , amount ,customer_name whose delivery date is 7th March and amount> average amount
select Customer.customer_id,amount,customer_name from 
Customer inner join Orders on 
Orders.customer_id=Customer.customer_id where 
    delivery_date="Mar 7, 2022" and 
    amount>(
    select avg(amount) from orders);


#Display delivery_date and total amount made at that day where toal amount>20000
select delivery_date,amt_dated from(
	select sum(amount) as amt_dated,
    delivery_date from orders 
	group by delivery_date) date_amt 
    where amt_dated>20000;

#find the name of customer who has spent the 3rd highst amount of money 
select customer_name,sum(amount)  as net_spent from customer c
join orders o on o.customer_id=c.customer_id
group by customer_name 
order by net_spent desc
limit 1 offset 2 ;

#find names of all the customer who ordered on 7th March through UPI and the amount spent by them
select distinct customer_name,sum(amount) over (partition by customer_name) as net_spent from customer c
join orders o on o.customer_id=c.customer_id
join invoice i on i.order_id=o.order_id
where delivery_date='Mar 7, 2022' and mode_of_pay='UPI';


#find id and names whose name contains i and order them in decreasing order of dish_ids
select Dish_ID,dish_name 
from Dish 
where prod_ID in
	(select prod_ID 
	from Product)
    and dish_name like "%i%" 
    order by Dish_ID desc;
    
#display customer name, delivery boy name and vehicle_type where age of customer is greater than average age of customer 
#and wallet balance is greater than 8000
select customer_name,boy_name,vehicle_type from
        Customer c join Delivery_boy d on
        c.Delivery_ID=d.Delivery_ID where 
        age>(
			select avg(age) from customer) 
				and wallet_balance>8000;

#display all orders that are delivered by car on a given date 
select count(*) as
orders_givendate_by_car,delivery_date from 
Orders where customer_id in 
(select customer_id FROM Delivery_Boy where vehicle_type="Car")
group by delivery_date
order by orders_givendate_by_car;

# display customer_name,gender,deliverboy_name,amount,delivery_date whose wallet balance is greater
# than 3000 and amount is greater than 3000
select customer_name,gender,boy_name,amount,delivery_date from
 customer join orders on orders.customer_id=customer.customer_id 
join Delivery_Boy d on d.customer_id=customer.customer_id where
	wallet_balance>3000 and amount>3000;
    
#increase amount of customers by 100 whose wallet balance is greater than 3000
update orders set amount=amount+100 
 where customer_id in 
 (select customer_id from Customer 
 where wallet_balance>3000);
 
 
#delete those invoices whose amount is less than average amount.
delete from invoice where 
	order_id in 
    (select order_id from Orders 
		where amount <= (
			select avg(amount) from Orders ));

 