def welcome():
    print("""  
  
               ___       ___   ___            ___     _________  ___        _    ___   _____   ___
     |      | |    |    |   | |   | |\    /| |            |     |   |      | \  |   |    |    |   |  \\   /
     |  /\  | |__  |    |     |   | | \  / | |__          |     |   |      |  | |___|    |    |___|    \\/
     | /  \ | |    |    |     |   | |  \/  | |            |     |   |      |  | |   |    |    | \\      |
     |/    \| |___ |___ |___| |___| |      | |___         |     |___|      |_/  |   |  __|__  |  \\     |

    """)

def login_information():
    print("""
        ##==========================================================================##  
        ||                                                                          ||
        ||                             SELECT YOUR CHOICE                           ||
        ||__________________________________________________________________________||                                    
        ||                                                                          ||
        ||                    1   IF YOU ARE A ADMIN                                ||
        ||                    2.  IF YOU ARE A EMPLOYEE                             ||                    
        ||                    3.  EXIT                                              ||                   
        ##==========================================================================##
    
    """)

def admin_menu():
    print("""
        ##==========================================================================##  
        ||                                                                          ||
        ||                             SELECT YOUR CHOICE                           ||
        ||__________________________________________________________________________||                                    
        ||                                                                          ||
        ||                    1   OLAP query 1                                      ||
        ||                    2.  OLAP query 2                                      ||
        ||                    3.  OLAP query 3                                      ||
        ||                    4.  OLAP query 4                                      ||                   
        ||                    5.  EXIT                                              ||
        ##==========================================================================## 
    
    """)

def employee_menu():
    print("""
        ##==========================================================================##  
        ||                                                                          ||
        ||                             SELECT YOUR CHOICE                           ||
        ||__________________________________________________________________________||                                    
        ||                                                                          ||
        ||                    1   Delivery by CAR                                   ||
        ||                    2.  Customer and del_boy                              ||
        ||                    3.  Give Cashback                                     ||
        ||                    4.  Give Discount                                     ||                   
        ||                    5.  EXIT                                              ||
        ##==========================================================================##     
    """)

# cube, rollup, grouping sets

from tabulate import tabulate

# l = [["Hassan", 21, "LUMS"], ["Ali", 22, "FAST"], ["Ahmed", 23, "UET"]]
# table = tabulate(l, headers=['Name', 'Age', 'University'], tablefmt='orgtbl')

# print(table)

import mysql.connector as mycon

check=mycon.connect(host="localhost",user="root",passwd="Raj@2003",database="Dairy_Model_1")
# if check.is_connected():
#     print("Connection successful")

data_cursor=check.cursor()


welcome()
while (True):
    login_information(); 
    
    x = int(input("Enter your choice: "))
    if (x == 1):
        while(True):
            password = int(input("enter your password: ")) # 1234 
            if (password == 1234):
                break
            else:
                print("!!entered wrong password!!\ntry again!!")
        print("Hello Admin!!")
        admin_menu()        #OLAP queries 
        admin_menu_option = int(input())
        if (admin_menu_option == 1):
        #     #having OLAP query1
            print("This query shows amount spent by a customer on a particular  delivery_date,  total amount spent on a particular delivery_date, and also the total amount spent")
            data_cursor.execute("select customer_name,delivery_date,sum(amount) from customer natural join orders GROUP BY delivery_date, customer_name with rollup;")
            data_obj = data_cursor.fetchall()
            table = tabulate(data_obj,headers = ['Sum','customer','delivery_date'], tablefmt = 'orgtbl')
            print(table)
            continue

        elif (admin_menu_option == 2):
        #     #having OLAP query2
            print("This query shows amount collected by a particular payment method on a particular date, total amount collected by a particular payment method and the total amount collected.")
            data_cursor.execute("""
                select mode_of_pay,delivery_date,sum(amount)
                from invoice natural join orders
                group by mode_of_pay, delivery_date with rollup;         
            """)

            data_obj = data_cursor.fetchall()
            table = tabulate(data_obj,headers = ['mode_of_pay','delivery_date','sum(amount)'],tablefmt = 'orgtbl')
            print(table)
        elif (admin_menu_option == 3):
            #having OLAP query3
            #pivot code
            print("this query runs to show the mode_of_payment statistics, with the age braces of the customers.")
            data_cursor.execute("""
                SELECT i.mode_of_pay,
                SUM(CASE WHEN c.age < 18 THEN o.amount ELSE 0 END) as '< 18',
                SUM(CASE WHEN c.age BETWEEN 18 AND 30 THEN o.amount ELSE 0 END) as '18-30',
                SUM(CASE WHEN c.age BETWEEN 31 AND 50 THEN o.amount ELSE 0 END) as '31-50',
                SUM(CASE WHEN c.age > 50 THEN o.amount ELSE 0 END) as '> 50'
                FROM orders o
                JOIN invoice i ON o.order_id = i.order_id
                JOIN customer c ON o.customer_id = c.customer_id
                GROUP BY i.mode_of_pay;             
            """)

            data_obj = data_cursor.fetchall()
            table = tabulate(data_obj,headers = ['mode_of_pay','<18','18-30','31-50','>50'],tablefmt = 'orgtbl')
            print(table)

        elif (admin_menu_option == 4):
        #     #HAVING OLAP query4
            #having slicing
            print("here we will run a code to find out the total payment made by adult males.")
            data_cursor.execute("""
                SELECT SUM(amount) as total_sales
                FROM orders o
                JOIN invoice i ON o.order_id = i.order_id
                JOIN customer c ON o.customer_id = c.customer_id
                WHERE  i.mode_of_pay = 'UPI' AND c.age > 18 AND c.Gender = "Male";
            """)
            data_obj = data_cursor.fetchall()
            # print(data_obj)
            for i in data_obj:
                for j in i:
                    print("total sales ="+str(int(j)))
            print()
        elif (admin_menu_option == 5):
            continue

    if (x == 2):
        while (True):
            password = int(input("Enter your password: "))
            if (password == 4321):
                break
            else: 
                continue
        print("Hello Employee!!")
        employee_menu()
        employee_option = int(input("Enter your option here: "))
        if (employee_option == 1):
            #Embeded Query 1
            print("display the no. of  orders that are delivered by car on a given date in increasing order of no. of orders by car")
            data_cursor.execute("""
            select count(*) as
            orders_givendate_by_car,delivery_date from 
            Orders where customer_id in 
            (select customer_id FROM Delivery_Boy where vehicle_type="Car")
            group by delivery_date
            order by orders_givendate_by_car;
            """)

            data_obj=data_cursor.fetchall()
            #fetchone()
            table = tabulate(data_obj,headers = ['no. of orders','delivery_date'], tablefmt = 'orgtbl')
            print(table)
            continue
        elif (employee_option == 2):
            #Embeded Query 2
            print("""
            Query to display customer name, delivery boy name and vehicle_type where age of customer is greater than average age of customer 
            and wallet balance is greater than 8000 :
            """)
            #transaction-3
            data_cursor.execute("""
            start transaction;
            select customer_name,boy_name,vehicle_type from
                    Customer c join Delivery_boy d on
                    c.Delivery_ID=d.Delivery_ID where 
                    age>(
                        select avg(age) from customer) 
                            and wallet_balance>8000;
            commit;
            """)

            data_obj=data_cursor.fetchall()
            #fetchone()
            table = tabulate(data_obj,headers = ['customer_name','boy_name','vehicle type'], tablefmt = 'orgtbl')
            print(table)
            continue
        elif (employee_option == 3):
            # trigger 1
            # we are giving discount of rupees 200 to the new orders, of each customers once they are done with new orders
            data_cursor.execute("drop trigger if exists cust_reward;")
            data_cursor.execute("""
                create trigger cust_reward
                before insert on orders 
                for each row 
                update customer SET wallet_balance=wallet_balance+200 WHERE customer_id=NEW.customer_id;
            """)

            # need to create checking the queries run properly
            print("wallet balance of the customer who added new order:")
            # showing customer 28, waller balance before adding  his new order in the dataset
            #transaction-4
            data_cursor.execute("""
                start transaction;
                select wallet_balance from customer where customer.customer_id = 28;  
                commit;           
            """)
            data_obj=data_cursor.fetchall()
            for i in data_obj:
                print(i)
            print()
            
            #-- inserting in orders
            data_cursor.execute("""
                insert into Orders (amount,delivery_date,time_stamps,customer_id) values (5420,"Mar 10, 2022","8:29 AM",28);
            """)

            #showing wallet balance after the new order got added into the dataset
            data_cursor .execute("""
                select wallet_balance from customer where customer. customer_id = 28;
            """)
            print("new wallet balance of the same customer after the order is added:")
            data_obj=data_cursor.fetchall()
            for i in data_obj:
                print(i)
            print()

            # data.execute("alter table orders auto_increment = 101;")
            # data.execute("delete FROM orders where order_id >= 101;")
            # data.execute("update customer SET wallet_balance = wallet_balance -400 where customer_id = 28;")

        elif (employee_option == 4):
            #trigger 2
            #we are giving dicount of 100 rupees who is paying using UPI as mode of payment
            data_cursor.execute("drop trigger if exists give_discount;")
            data_cursor.execute("""
                create trigger give_discount
                before insert on invoice
                for each row
                update orders SET orders.amount = orders.amount - 100 Where NEW.order_id = orders.order_id         
            """)

            # need to check the query functionality

            # entering the order 101
            #transaction-1
            data_cursor.execute('''
            start transaction;
            insert into orders (amount,delivery_date,time_stamps,customer_id) values (7880,\"Mar 10, 2022\",\"10:22 PM\",41);
            commit;
            '''
            )
            # showing the order amount before the payment is made
            data_cursor.execute("select amount from orders where order_id = 101;")
            print("Order value of the new order: ")
            data_obj=data_cursor.fetchall()
            for i in data_obj:
                print(i)
            print()

            # -- inserting the invoice 
            #transaction-2
            data_cursor.execute("start transaction;")
            data_cursor.execute("insert into invoice values (\"UPI\",\"vitae@yahoo.net\",101);")
            # -- once the amount is added, we can see a measurable change in the amount section in the orders table
            data_cursor.execute("select amount from orders where order_id = 101;")
            data_cursor.execute("commit;")

            data_obj = data_cursor.fetchall()
            print("new order value: ")
            for i in data_obj:
                print(i)
            print()

            # data.execute("alter table orders auto_increment = 101;")
            # data.execute("delete FROM orders where order_id >= 101;")
            # data.execute("delete from invoice where order_id >= 101;")
            # data.execute("update customer SET wallet_balance = wallet_balance -400 where customer_id = 28;")

        elif (employee_option == 5):
            continue #


    
    if (x == 3):
        break


data_cursor.close()
check.close()

#slicing 
#dicing
#piviot
#rollup
