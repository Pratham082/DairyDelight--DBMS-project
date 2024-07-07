class customer:
    order_id = 0

    def __init__(self, arr):
        self.name = arr[1]
        self.id = arr[0]
        self.age = arr[2]
        self.gender = arr[3]
        self.emailid = arr[4]
        self.contact = arr[5]
        self.address = arr[6]
        self.wallet = arr[7]
        self.delid = arr[8]

    def sout(self):
        print("name: " + self.name)
        print("contact information: " + self.contact)
        print("age: " + self.age)
        print("email id: " + self.emailid)
        print("address: " + self.address)

    def invoice(self, Order_ID, Time_Stamp, mode_of_pay, email_id, amount, del_date):
        print(
            f"""

            ##===================================================================================================##
            ||                                    Dairy Delight Private Limited                                  ||
            ||                                     Online Reciept cum Invoice                                    ||
                                                          {Time_Stamp}                                   
                                                Order value = {amount}
                                                Mode of payment = {mode_of_pay}
                                                Email_ID = {email_id}
                                                Order ID = {Order_ID}
                                                Delivery Date = {del_date}
            ||                                  Payment Successfull!!                                            ||
            ||                                  Thank you shopping with us!!                                     ||
            ##===================================================================================================##
        
        
        """
        )


class category:
    def __init__(self, arr):
        self.cat_id = arr[0]
        self.cat_name = arr[1]
        self.cat_tagline = arr[2]
        self.cat_ingredient = arr[3]


class product:
    prod_qty_purchase = 0

    def __init__(self, arr):
        self.prod_id = arr[0]
        self.prod_name = arr[1]
        self.prod_qty = arr[2]
        self.shelf_life = arr[3]
        self.price = arr[4]
        self.store_inst = arr[5]
        self.category_id = arr[6]

    def add_quantity(self, q):
        self.prod_qty_purchase = q

    def print_details(self):
        print(
            f"""
            ##======================================================================================================##
                                                Product Name: {self.prod_name}                                      
                                                Product ID: {self.prod_id}                                          
                                                Quantitiy: {self.prod_qty}                                          
                                                Price: {self.price}                                                 
                                                Shelf Life: {self.shelf_life}                                       
                                                Storage Instruction: {self.store_inst}                              
                                                                                                                  
            ##======================================================================================================##     
        

        """
        )


class cart:
    cart_list = []
    tot = 0

    def __init__(self, element):
        self.cart_list.append(element)

    def show_cart(self):
        if self.cart_list == None:
            print(
                "\n\n\t\t\tYour cart is empty!!\n\t\t\tPlease Enjoy shopping with us!!\n\n"
            )
        else:
            list_ = []
            head = ["Sno.", "Name", "Qty", "Price", "Total"]
            self.tot = 0
            for i in self.cart_list:
                self.tot = self.tot + i.prod_qty_purchase * i.price
                l = [
                    self.cart_list.index(i) + 1,
                    i.prod_name,
                    i.prod_qty_purchase,
                    i.price,
                    i.prod_qty_purchase * i.price,
                ]
                list_.append(l)
            table = tabulate(list_, headers=head, tablefmt="orgtbl")
            print(table)
            print("TOTAL AMT = " + str(self.tot) + " rupees only")


def welcome():
    print(
        """  
  
               ___       ___   ___            ___     _________  ___        _    ___   _____   ___
     |      | |    |    |   | |   | |\    /| |            |     |   |      | \  |   |    |    |   |  \\   /
     |  /\  | |__  |    |     |   | | \  / | |__          |     |   |      |  | |___|    |    |___|    \\/
     | /  \ | |    |    |     |   | |  \/  | |            |     |   |      |  | |   |    |    | \\      |
     |/    \| |___ |___ |___| |___| |      | |___         |     |___|      |_/  |   |  __|__  |  \\     |

    """
    )


def login_information():
    print(
        """
        ##==========================================================================##  
        ||                                                                          ||
        ||                             SELECT YOUR CHOICE                           ||
        ||__________________________________________________________________________||                                    
        ||                                                                          ||
        ||                    1   IF YOU ARE AN ADMIN                               ||
        ||                    2.  IF YOU ARE A CUSTOMER                             ||                    
        ||                    3.  EXIT                                              ||                   
        ##==========================================================================##
    
    """
    )


def customer_menu():
    print(
        """
        ##==========================================================================##  
        ||                                                                          ||
        ||                             SELECT YOUR CHOICE                           ||
        ||__________________________________________________________________________||                                    
        ||                                                                          ||
        ||                    1   Explore                                           ||
        ||                    2.  Proceed to cart                                   ||
        ||                    3.  Wallet Balance                                    ||            
        ||                    4.  Check Order                                       ||
        ||                    5.  Print Invoice                                     ||
        ||                    6.  Payment of Order                                  ||
        ||                    7.  Check Discount Coupons                            ||
        ||                    8. Order From Shop                                    ||
        ||                    9. Nearest Shop                                       ||
        ||                    10. Check Dishes                                      ||
        ||                    11. EXIT                                              ||
        ##==========================================================================##     
    """
    )


def admin_menu():
    print(
        """
        ##==========================================================================##  
        ||                                                                          ||
        ||                             SELECT YOUR CHOICE                           ||
        ||__________________________________________________________________________||                                    
        ||                                                                          ||
        ||                    1   Customer and Delivery                             ||
        ||                    2.  Amount collected and mode of payment              ||
        ||                    3.  Age and mode of payment                           ||
        ||                    4.  Adult males and payment                           ||
        ||                    5.  Delivery by CAR                                   ||
        ||                    6.  Customer and del_boy                              ||
        ||                    7.  Give Cashback                                     ||
        ||                    8.  Give Discount                                     ||                   
        ||                    9.  EXIT                                              ||                                       
        ##==========================================================================## 
    
    """
    )


import datetime

current_time = datetime.datetime.now()

time_stamp = current_time.timestamp()

from tabulate import tabulate
import mysql.connector as mycon

check = mycon.connect(
    host="localhost", user="root", passwd="Raj@2003", database="Dairy_Model_1"
)
data_cursor = check.cursor()


welcome()
while True:
    login_information()

    x = int(input("Enter your choice: "))
    if x == 1:
        while True:
            password = int(input("enter your password: "))  # 1234
            if password == 1234:
                break
            else:
                print("!!entered wrong password!!\ntry again!!")
        print("Hello Admin!!")
        admin_menu()  # OLAP queries
        admin_menu_option = int(input())
        if admin_menu_option == 1:
            # Customer and Delivery
            print(
                "This query shows amount spent by a customer on a particular  delivery_date,  total amount spent on a particular delivery_date, and also the total amount spent"
            )
            data_cursor.execute(
                "select customer_name,delivery_date,sum(amount) from customer natural join orders GROUP BY delivery_date, customer_name with rollup;"
            )
            data_obj = data_cursor.fetchall()
            table = tabulate(
                data_obj,
                headers=["Sum", "customer", "delivery_date"],
                tablefmt="orgtbl",
            )
            print(table)
            continue

        elif admin_menu_option == 2:
            # Amount collected and mode of payment
            print(
                "This query shows amount collected by a particular payment method on a particular date, total amount collected by a particular payment method and the total amount collected."
            )
            data_cursor.execute(
                """
                select mode_of_pay,delivery_date,sum(amount)
                from invoice natural join orders
                group by mode_of_pay, delivery_date with rollup;         
            """
            )
            data_obj = data_cursor.fetchall()
            table = tabulate(
                data_obj,
                headers=["mode_of_pay", "delivery_date", "sum(amount)"],
                tablefmt="orgtbl",
            )
            print(table)
            continue

        elif admin_menu_option == 3:
            # Age and mode_of_payment
            print(
                "this query runs to show the mode_of_payment statistics, with the age braces of the customers."
            )
            data_cursor.execute(
                """
                SELECT i.mode_of_pay,
                SUM(CASE WHEN c.age < 18 THEN o.amount ELSE 0 END) as '< 18',
                SUM(CASE WHEN c.age BETWEEN 18 AND 30 THEN o.amount ELSE 0 END) as '18-30',
                SUM(CASE WHEN c.age BETWEEN 31 AND 50 THEN o.amount ELSE 0 END) as '31-50',
                SUM(CASE WHEN c.age > 50 THEN o.amount ELSE 0 END) as '> 50'
                FROM orders o
                JOIN invoice i ON o.order_id = i.order_id
                JOIN customer c ON o.customer_id = c.customer_id
                GROUP BY i.mode_of_pay;             
            """
            )

            data_obj = data_cursor.fetchall()
            table = tabulate(
                data_obj,
                headers=["mode_of_pay", "<18", "18-30", "31-50", ">50"],
                tablefmt="orgtbl",
            )
            print(table)
            continue

        elif admin_menu_option == 4:
            # adult males and payment
            print(
                "here we will run a code to find out the total payment made by adult males."
            )
            data_cursor.execute(
                """
                SELECT SUM(amount) as total_sales
                FROM orders o
                JOIN invoice i ON o.order_id = i.order_id
                JOIN customer c ON o.customer_id = c.customer_id
                WHERE  i.mode_of_pay = 'UPI' AND c.age > 18 AND c.Gender = "Male";
            """
            )
            data_obj = data_cursor.fetchall()
            # print(data_obj)
            for i in data_obj:
                for j in i:
                    print("total sales =" + str(int(j)))
            print()
            continue

        elif admin_menu_option == 5:
            # Adding Category
            print(
                "display the no. of  orders that are delivered by car on a given date in increasing order of no. of orders by car"
            )
            data_cursor.execute(
                """
            select count(*) as
            orders_givendate_by_car,delivery_date from 
            Orders where customer_id in 
            (select customer_id FROM Delivery_Boy where vehicle_type="Car")
            group by delivery_date
            order by orders_givendate_by_car;
            """
            )

            data_obj = data_cursor.fetchall()
            # fetchone()
            table = tabulate(
                data_obj, headers=["no. of orders", "delivery_date"], tablefmt="orgtbl"
            )
            print(table)
            continue

        elif admin_menu_option == 6:
            # Give Discount
            print(
                """
            Query to display customer name, delivery boy name and vehicle_type where age of customer is greater than average age of customer 
            and wallet balance is greater than 8000 :
            """
            )
            # transaction-3
            data_cursor.execute(
                """select customer_name,boy_name,vehicle_type from
                    Customer c join Delivery_boy d on
                    c.Delivery_ID=d.Delivery_ID where 
                    age>(
                        select avg(age) from customer) 
                            and wallet_balance>8000;"""
            )

            data_obj = data_cursor.fetchall()
            # fetchone()
            table = tabulate(
                data_obj,
                headers=["customer_name", "boy_name", "vehicle type"],
                tablefmt="orgtbl",
            )
            print(table)
            continue

        elif admin_menu_option == 7:
            # Give Reward
            data_cursor.execute("drop trigger if exists cust_reward;")
            data_cursor.execute(
                """
                create trigger cust_reward
                before insert on orders 
                for each row 
                update customer SET wallet_balance=wallet_balance+200 WHERE customer_id=NEW.customer_id;
            """
            )

            # need to create checking the queries run properly
            print("wallet balance of the customer who added new order:")
            # showing customer 28, waller balance before adding  his new order in the dataset
            # transaction-4
            data_cursor.execute("start transaction")
            data_cursor.execute(
                """
                select wallet_balance from customer where customer.customer_id = 28;  
            """
            )
            data_obj = data_cursor.fetchall()
            for i in data_obj:
                print(i)
            print()

            # -- inserting in orders
            data_cursor.execute(
                """
                insert into Orders (amount,delivery_date,time_stamps,customer_id) values (5420,"Mar 10, 2022","8:29 AM",28);
            """
            )

            # showing wallet balance after the new order got added into the dataset
            data_cursor.execute(
                """
                select wallet_balance from customer where customer. customer_id = 28;
            """
            )
            print("new wallet balance of the same customer after the order is added:")
            data_obj = data_cursor.fetchall()
            for i in data_obj:
                print(i)
            print()
            data_cursor.execute("commit")

            # data.execute("alter table orders auto_increment = 101;")
            # data.execute("delete FROM orders where order_id >= 101;")
            # data.execute("update customer SET wallet_balance = wallet_balance -400 where customer_id = 28;")

            continue

        elif admin_menu_option == 8:
            # statisitcs
            # trigger 2
            # we are giving dicount of 100 rupees who is paying using UPI as mode of payment
            data_cursor.execute("drop trigger if exists give_discount;")
            data_cursor.execute(
                """
                create trigger give_discount
                before insert on invoice
                for each row
                update orders SET orders.amount = orders.amount - 100 Where NEW.order_id = orders.order_id         
            """
            )

            # need to check the query functionality

            # entering the order 101
            # transaction-1
            data_cursor.execute("start transaction;")
            data_cursor.execute(
                'insert into orders (amount,delivery_date,time_stamps,customer_id) values (7880,"Mar 10, 2022","10:22 PM",41);'
            )
            data_cursor.execute("commit;")
            # showing the order amount before the payment is made
            data_cursor.execute("select amount from orders where order_id = 101;")
            print("Order value of the new order: ")
            data_obj = data_cursor.fetchall()
            for i in data_obj:
                print(i)
            print()

            # -- inserting the invoice
            # transaction-2
            data_cursor.execute("start transaction;")
            data_cursor.execute(
                'insert into invoice values ("UPI","vitae@yahoo.net",101);'
            )
            # -- once the amount is added, we can see a measurable change in the amount section in the orders table
            data_cursor.execute("select amount from orders where order_id = 101;")

            data_obj = data_cursor.fetchall()
            print("new order value: ")
            for i in data_obj:
                print(i)
            print()

            # data.execute("alter table orders auto_increment = 101;")
            # data.execute("delete FROM orders where order_id >= 101;")
            # data.execute("delete from invoice where order_id >= 101;")
            # data.execute("update customer SET wallet_balance = wallet_balance -400 where customer_id = 28;")
            data_cursor.execute("commit;")

            continue

        elif admin_menu_option == 9:
            continue

    if x == 2:
        print(
            """
            ##================================================================================##
            ||              CHOOSE THE FOLLOWING OPTIONS:                                     ||
            ||              1. IF YOU ARE AN EXISTING USER                                    ||
            ||              2. IF YOU ARE NEW USER                                            ||
            ||                                                                                ||
            ##================================================================================##
        """
        )
        # customer_ = customer()
        while True:
            login = int(input("Enter your preference here: "))
            if login == 1:  # existing user
                print("\n\n\t\t\tHello exixting user!!\n\n")
                name = input("Enter your Name: ")
                id = int(input("enter your customer_id: "))
                data_cursor.execute(
                    "select * from customer where customer.customer_id = "
                    + str(id)
                    + ""
                )
                data_obj = data_cursor.fetchall()
                for i in data_obj:
                    customer_ = customer(i)
                print(
                    "\n\n\t\t\tHELLO "
                    + customer_.name
                    + " WELCOME TO DAIRY DELIGHT!!\n\n"
                )
                print(
                    "\n\n##################### Login successfull!! please feel free to explore!!###############\n\n"
                )
                break
            if login == 2:
                print(
                    "\n\n\t\t\tnot to worry!! enter you credentials below and get registered today.\n\n"
                )
                name = str(input("Enter your name: "))
                age = int(input("enter your age: "))
                gender = input("enter your gender: ")
                email = input("enter your emailid: ")
                contact = int(input("enter your conatact number: "))
                address = input("enter your address: ")
                customer_ = customer(
                    [100000, name, age, gender, email, contact, address, 0, 2]
                )
                data_cursor.execute(
                    f'INSERT INTO customer(customer_name,age,Gender,email_id,contact_number,address,wallet_balance,Delivery_ID) VALUES("{name}",{age},"{gender}","{email}","{contact}","{address}",0,2)'
                )
                check.commit()
                data_cursor.execute(
                    f'select customer_id from customer where customer_name = "{name}";'
                )
                data_obj = data_cursor.fetchall()
                customer_.id = data_obj[0]
                print("your customer_id : " + str(customer_.id))
                print(
                    "\n\n\t\t\tYou are successfully registered with us, shop with us today to get registered on our database and enjoy unending deals\n\n"
                )
                break
            else:
                print("\n\n\t\t\twrong value, try again\n\n")

        # reaching here means that the customer has been assigned data in customer class.
        while True:
            password = int(input("Enter your password: "))  # 4321
            if password == 4321:
                break
            else:
                print("\n\n\t\t\tYou have entered wrong password! Try Again\n\n")
        print("\n\n\t\t\tHello Customer!!\n\n")
        cart_of_customer = None
        while True:
            customer_menu()
            customer_option = int(input("Enter your option here: "))
            if customer_option == 1:
                # Explore
                cat = []
                return_to_category = 1
                while return_to_category:
                    return_to_category = 0
                    data_cursor.execute("select * from category;")
                    data_obj = data_cursor.fetchall()
                    for i in data_obj:
                        cat.append(category(i))
                    print("\n\n")
                    table = tabulate(
                        data_obj,
                        headers=["category_id", "category", "Tagline", "Ingredient"],
                        tablefmt="orgtbl",
                    )
                    print(table)
                    print(
                        "\n\t\t\tselect the corresponding option to explore further\n"
                    )
                    category_option = int(input("enter your option here: "))
                    return_to_products = 1
                    category_chosen = None
                    for i in cat:
                        if category_option == i.cat_id:
                            category_chosen = i
                    if category_chosen == None:
                        if category_option == 1099:
                            print("you are exiting to the previous menu.")
                            return_to_category = 0
                            break
                        print(
                            "\n\n\t\t\t You have choosen wrong option, please try again.\n\n"
                        )
                        return_to_category = 1
                        continue
                    while return_to_products:
                        print(
                            "\n\n\t\t\tHere you have choosen CATEGORY = "
                            + category_chosen.cat_name
                            + ". Explore it below!!\n\n"
                        )
                        data_cursor.execute(
                            "select prod_id, product_name from product where product.category_id = "
                            + str(category_chosen.cat_id)
                            + ";"
                        )
                        data_obj = data_cursor.fetchall()
                        table = tabulate(
                            data_obj, headers=["Product ID", "Name"], tablefmt="orgtbl"
                        )
                        print(table)
                        data_cursor.execute(
                            "select * from product where category_id = "
                            + str(category_chosen.cat_id)
                            + ";"
                        )
                        data_obj = data_cursor.fetchall()
                        product_list = []
                        for i in data_obj:
                            product_list.append(product(i))
                        print(
                            "\n\n\t\t\tIf you wish to Exit enter 1099 in the Input prompt any time.\n\n"
                        )
                        product_chosen = int(
                            input(("Enter product ID to explore further: "))
                        )
                        if product_chosen == 1099:
                            return_to_category = 1
                            break
                        for i in product_list:
                            if product_chosen == i.prod_id:
                                i.print_details()
                                print(
                                    "\n\n\t\t\tDo you want to buy this product?\n\t\t\t1. Yes\n\t\t\t2. No\n\n"
                                )
                                confirm = int(input("enter your input here: "))
                                if confirm == 1:
                                    quantity = int(
                                        input(
                                            "enter the quantity you want to purchase: "
                                        )
                                    )
                                    i.add_quantity(quantity)
                                    cart_of_customer = cart(i)
                                    print("\n\n\t\t\tProduct added successfuly!!\n")
                                    input("\t\t\t Press Enter to go  back! \n\n")
                                else:
                                    return_to_products = 1
                                    continue

            elif customer_option == 2:
                # Proceed to cart
                while True:
                    if cart_of_customer == None:
                        print("first add to cart sommething by exploring the menu")
                        input("press enter to go back to the previous menu")
                        break
                    cart_of_customer.show_cart()
                    print(
                        "\n\n\t\t\t1. Contiune to buy the items in your cart\n\t\t\t2. Edit Cart\n\t\t\t3. Continue to previous menu: "
                    )
                    cont = int(input("Enter your option:  "))
                    if cont == 1:  # oredering the order
                        if cart.tot <= customer_.wallet:
                            # proceed to check out
                            print("total amount payable = " + str(cart_of_customer.tot))
                            print("Your wallet balance = " + str(customer_.wallet))
                            if cart_of_customer.tot > customer_.wallet:
                                print(
                                    "Your order value is more than the available balance in your wallet"
                                )
                                # print(
                                #     "\n\n\t\t\t Choose the mode of payment!\n\t\t\t1. UPI\n\t\t\t2. Cash on Delivery\n\t\t\t3. Card Payment\n\n"
                                # )
                                mode_of_pay = input("Press enter to continue ")
                            else:
                                from datetime import datetime

                                date_time = datetime.fromtimestamp(time_stamp)
                                str_date = date_time.strftime(" %B %d, %Y")
                                str_time = date_time.strftime("%I:%M %p")
                                data_cursor.execute(
                                    f"  INSERT INTO orders (amount,delivery_date,time_stamps,customer_id) VALUES ({cart_of_customer.tot},'{str_date}','{str_time}',{customer_.id});"
                                )
                                check.commit()
                                data_cursor.execute(
                                    f"select order_id from orders where orders.time_stamps = '{str_time}';"
                                )
                                customer_.order_id = int(data_cursor.fetchall()[0][0])
                                data_cursor.execute(
                                    f'  INSERT INTO invoice VALUES ("UPI","{customer_.emailid}",{customer_.order_id});'
                                )
                                check.commit()
                                print("ordered successfully!1")
                                input("press enter to coninue")
                            break
                    elif cont == 2:  # editing the cart
                        print(
                            "\n\n\t\t\tEnter what operation you want to do:\n\t\t\t1. Change the quantity\n\t\t\t2. Delete the item"
                        )
                        edit_opt = int(input("enter your choice here: "))
                        if edit_opt == 1:
                            cart_of_customer.show_cart()
                            pro = int(
                                input(
                                    "which product you want to alter quantity of? Enter Serial no.: "
                                )
                            )
                            if pro > len(cart_of_customer.cart_list):
                                print("mentioned wrong input")
                                print("exixting the whole process!")
                                input("press enter to continue")
                                break
                            product_edit = cart_of_customer.cart_list[pro - 1]
                            number = int(
                                input("enter the new number you want to put: ")
                            )

                            if number <= 0:
                                cart_of_customer.cart_list.remove(product_edit)
                                print("product removed successfully!!")
                                input("press enter to go back")
                            else:
                                cart_of_customer.cart_list[
                                    pro - 1
                                ].prod_qty_purchase = number
                                print("successfully done the requisite action!!")
                                input("press enter to exit to the previous menu!!")
                            break
                        elif edit_opt == 2:
                            cart_of_customer.show_cart()
                            pro = int(
                                input(
                                    "which product you want to delete? Enter Serial no.: "
                                )
                            )
                            if pro > len(cart_of_customer.cart_list):
                                print("mentioned wrong input")
                                print("exixting the whole process!")
                                input("press enter to continue")
                                break
                            cart_of_customer.cart_list.remove(
                                cart_of_customer.cart_list[pro - 1]
                            )
                            print("successfully deleted")
                            input("press enter to go back to the previous menu.")
                            break
                        break
                    elif cont == 3:  # exiting
                        break
                    else:
                        print("Wrong option entered try again")
                        continue
                continue
            elif customer_option == 3:
                # Check Wallet Balance
                print(f"\n\n\t\t\twallet balance : {customer_.wallet} \n\n")
                print(
                    "\n\n\t\t\t Enter the following options to perform the operations\n\t\t\t 1. Add Balance \n\t\t\t 2. Exit"
                )
                wallet_update = int(input("Enter the value of your selection here: "))
                if wallet_update == 1:
                    # code to update wallet balance
                    add_balance = int(input("Enter the amount you want to enter: "))
                    data_cursor.execute(
                        "update customer SET wallet_balance = wallet_balance + "
                        + str(add_balance)
                        + " where customer_id = "
                        + str(customer_.id)
                        + ";"
                    )
                    check.commit()
                    customer_.wallet += add_balance
                    print("wallet balance updated!!")
                    input("press enter to go back to previous menu")
                    continue
                else:
                    continue

            elif customer_option == 4:
                # check order
                data_cursor.execute(
                    f"select order_id,amount,delivery_date,time_stamps from orders where orders.customer_id = {customer_.id};"
                )
                data_obj = data_cursor.fetchall()
                table = tabulate(
                    data_obj,
                    headers=["Order ID", "Amount", "Delivery Date", "Time Stamp"],
                    tablefmt="orgtbl",
                )
                print(table)
                cont = input("press enter to go back to previous menu : ")
                continue

            elif customer_option == 5:
                # print invoice
                order_id = int(
                    input("enter the order_id of the order you need invoice of: ")
                )
                if order_id == 1099:
                    continue
                data_cursor.execute(
                    f"select * from invoice where order_id = {order_id};"
                )
                invoice = data_cursor.fetchall()[0]
                mode_of_pay = invoice[0]
                email_id = invoice[1]
                data_cursor.execute(
                    f"select amount, delivery_date, time_stamps from orders where orders.order_id = {order_id};"
                )
                invoice = data_cursor.fetchall()[0]
                amount = invoice[0]
                del_date = invoice[1]
                time_stamp = invoice[2]
                customer_.invoice(
                    order_id, time_stamp, mode_of_pay, email_id, amount, del_date
                )
                input("press enter to go  to previous menu!!")
                continue

            elif customer_option == 6:
                # payment of order
                print("go to cart to complete the payment.")
                input("press enter to continue.")
                continue
            elif customer_option == 7:
                # check discount coupons
                # trigger statement for cashback if paid through upi
                print(
                    "\n\n\t\t\tDISCOUNT 1\n\t\t\tCashback to the users who have paid through UPI as a mode of payment \n\n"
                )
                # trigger statement for 200 discount for ordering second time
                print(
                    "\n\n\t\t\tDISCOUNT 2\n\t\t\t200 rupees off on the second order\n"
                )
                input("Press Enter to go back to the previous menu.")
                continue

            elif customer_option == 8:
                # order from shop
                data_cursor.execute(
                    "select Shop_ID, address, salesman, inventory from shop;"
                )
                data_obj = data_cursor.fetchall()
                print("\n\n")
                table = tabulate(
                    data_obj,
                    headers=["shop no.", "Address", "Owner", "inventory"],
                    tablefmt="orgtbl",
                )
                print(table)
                print("\n\n")
                cont = input("press enter to go to previous menu")
                continue

            elif customer_option == 9:
                # nearest shop
                data_cursor.execute("select Shop_ID, address from shop;")
                data_obj = data_cursor.fetchall()
                print("\n\n")
                table = tabulate(
                    data_obj, headers=["shop no.", "Address"], tablefmt="orgtbl"
                )
                print(table)
                print("\n\n")
                cont = input("press enter to go to previous menu")
                continue
            elif customer_option == 10:
                # Check Dishes
                data_cursor.execute(
                    "select Dish_ID, dish_name, product_name from Dish JOIN product where dish.prod_id = product.prod_id;"
                )
                data_obj = data_cursor.fetchall()
                table = tabulate(
                    data_obj,
                    headers=["Sno.", "Dish Name", "Product it is made from"],
                    tablefmt="orgtbl",
                )
                print(table)
                cont = int(input("press 1 to coninue to previous menu"))
                continue
            elif customer_option == 11:
                # Exit
                break

    if x == 3:
        break


data_cursor.close()
check.close()
