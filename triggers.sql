use Dairy_Model_1;

create trigger cust_reward
before insert on orders 
for each row 
update customer SET wallet_balance=wallet_balance+200 WHERE customer_id=NEW.customer_id;

drop trigger if exists amt_change

 delimiter //
 CREATE TRIGGER amt_change BEFORE insert ON invoice
       FOR EACH ROW
       BEGIN
           IF NEW.mode_of_pay ="UPI" THEN
               update orders SET amount=amount-100 WHERE orders.order_id=NEW.order_id;
           END IF;
       END //
	   delimiter ;
