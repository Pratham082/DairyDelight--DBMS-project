#show databases;
#drop database Dairy_Model_1;
Create Database Dairy_Model_1; 
use Dairy_Model_1;

CREATE TABLE Customer(
	customer_id int Not Null auto_increment,
    customer_name varchar(200),
    age int,
    Gender varchar(50),
    email_id varchar(200),
    contact_number varchar(50),
    address varchar(200),
    wallet_balance float,
    Delivery_ID int,
    primary key(customer_id)
);
-- select * from customer;


# data entered for customer


CREATE TABLE Category(
	category_id int unsigned not null auto_increment,
    category_name varchar(200),
    tagline varchar(200),
    Ingredient varchar(200),
    primary key(category_id)
);

#select * from category;


#data eneterd for category

CREATE TABLE shop(
	Shop_ID int unsigned not null auto_increment,
    address varchar(200),
    salesman varchar(200),
    inventory int,
    customer_id int,
    primary key(Shop_ID)
);

#select * from shop;
#data eneterd for shop



CREATE TABLE Owners(
	owner_name varchar(200),
    mobile varchar(50),
    email_id varchar(200),
    Shop_ID int
);

#select * from Owners;
#data entered for owners


-- drop table Delivery_Boy;
CREATE TABLE Delivery_Boy(
	Delivery_ID int unsigned not null auto_increment,
    boy_name varchar(200),
    mobile varchar(50),
    vehicle_type varchar(100),
    vehicle_num varchar(100),
	customer_id int,
    Shop_ID int,
	primary key(Delivery_ID)
);

#select * from Delivery_Boy; 
#table created and data entered for delivery_boy

#drop table invoice;
Create table invoice(
	mode_of_pay varchar(100),
    email_id varchar(200),
    order_id int
);

#select * from invoice;
#table created and data enetered



CREATE TABLE Orders(
	order_id int unsigned not null auto_increment,
    amount int,
    delivery_date varchar(200),
    time_stamps varchar(200),
    customer_id int,
    primary key(order_id)
);

#select * from orders;
#table created and data enetered



CREATE TABLE Product(
	prod_id int unsigned not null auto_increment,
    product_name varchar(200),
    quantity int,
    shelf_life float,
    Price int,
    store_inst varchar(200),
    category_id int,
    primary key(prod_id)
);
#select * from Product;
#table created and data inserted



CREATE TABLE Dish(
	Dish_ID int unsigned not null auto_increment,
	dish_name varchar(200),
	prod_id int,
	primary key(Dish_ID)
);

#select * from dish;
#table created and data entered


#created indexes for faster data access
create index product_idx
on product (product_name,price);

create index del_idx
on Delivery_Boy(boy_name,vehicle_type);

create index customer_idx
on Customer (customer_name,age,Gender,wallet_balance);

Alter table Dish
modify prod_id int unsigned;
alter table dish
add foreign key(prod_id) references product(prod_id);
#dish table - foreign key introduce - prod_id


Alter table product
modify category_id int unsigned;
alter table product
add foreign key(category_id) references Category(category_id);
#product table - foreign key introduce - category_id


alter table orders
add foreign key(customer_id) references customer(customer_id);
#orders table - foreign key introduce - customer_id


Alter table invoice
modify order_id int unsigned;
alter table invoice
add foreign key(order_id) references orders(order_id);
#invoice table - foreign key introduce - order_id


Alter table owners
modify Shop_ID int unsigned;
alter table owners
add foreign key(Shop_ID) references shop(Shop_ID);
#owners table - foreign key introduce - shop_id

alter table shop
add foreign key(customer_id) references customer(customer_id);
#shop table - foreign key introduce - customer_id


Alter table customer
modify Delivery_ID int unsigned;
alter table customer
add foreign key(Delivery_ID) references Delivery_Boy(Delivery_ID);
#customer table - foreign key introduce - Delivery_id

Alter table Delivery_Boy
modify Shop_ID int unsigned;
Alter table Delivery_Boy
modify customer_id int unsigned;
Alter table Delivery_Boy
modify customer_id int;
alter table delivery_boy
add foreign key(Shop_ID) references shop(Shop_ID);
alter table delivery_boy
add foreign key(customer_id) references customer(customer_id);
#delivery_boy table - foreign key introduce - shop_id
#delivery_boy - foreign key introduce - customer_id