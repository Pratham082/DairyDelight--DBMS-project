
# Dairy Delight

Dairy Delight is a project developed as part of a Database Management System (DBMS) course. It is designed to manage customer information, handle orders, generate invoices, and manage dairy product categories for a fictional dairy delivery service.

## Features

- **Customer Management**: Add and maintain customer information.
- **Order Processing**: Process orders and update customer wallets.
- **Invoice Generation**: Generate and print invoices for completed orders.
- **Category Management**: Manage different categories of dairy products.

## Structure

### Classes

1. **Customer**
   - Manages customer information such as name, ID, age, gender, email, contact number, address, wallet balance, and delivery ID.
   - Methods:
     - `__init__(self, arr)`: Initializes a customer object with provided details.
     - `sout(self)`: Prints customer details.
     - `invoice(self, Order_ID, Time_Stamp, mode_of_pay, email_id, amount, del_date)`: Generates an invoice for a customer order.

2. **Category**
   - Manages dairy product categories.
   - Methods:
     - `__init__(self, arr)`: Initializes a category object with provided details.

3. **Order**
   - Manages order details.
   - Methods:
     - `__init__(self, arr)`: Initializes an order object with provided details.

## Usage

1. **Customer Management**
   - Create a new customer: `customer_instance = customer(arr)`
   - Print customer details: `customer_instance.sout()`
   - Generate an invoice: `customer_instance.invoice(Order_ID, Time_Stamp, mode_of_pay, email_id, amount, del_date)`

2. **Category Management**
   - Create a new category: `category_instance = category(arr)`

3. **Order Management**
   - Create a new order: `order_instance = order(arr)`

## Example

Here is an example of how to use the `Customer` class:

```python
# Initialize customer
customer_data = [1, "John Doe", 25, "Male", "john.doe@example.com", "1234567890", "123 Main St", 100.0, 101]
customer_instance = customer(customer_data)

# Print customer details
customer_instance.sout()

# Generate an invoice
customer_instance.invoice(12345, "2023-07-01 10:00:00", "Credit Card", "john.doe@example.com", 50.0, "2023-07-05")
```

## Installation

To use this project, simply clone the repository and run the provided Python script.

```bash
git clone <repository_url>
cd Dairy_Delight
python Dairy_Delight_Interface.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
