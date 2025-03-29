import mysql.connector
import pandas as pd

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change if needed
        password="password",  # Change if needed
        database="order_db"
    )

def add_customer(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()
    print("Customer added successfully!")

def view_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    for customer in cursor.fetchall():
        print(customer)
    conn.close()

def delete_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
    conn.commit()
    conn.close()
    print("Customer deleted successfully!")


def add_product(name, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
    conn.commit()
    conn.close()
    print("Product added successfully!")

def view_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    for product in cursor.fetchall():
        print(product)
    conn.close()


def add_order(customer_id, product_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)", 
                   (customer_id, product_id, quantity))
    conn.commit()
    conn.close()
    print("Order placed successfully!")

def view_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT orders.id, customers.name, products.name, orders.quantity FROM orders "
                   "JOIN customers ON orders.customer_id = customers.id "
                   "JOIN products ON orders.product_id = products.id")
    for order in cursor.fetchall():
        print(order)
    conn.close()


def update_order_quantity(order_id, new_quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET quantity = %s WHERE id = %s", (new_quantity, order_id))
    conn.commit()
    conn.close()
    print("Order quantity updated successfully!")


while True:
    print("\nOrder Management System")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Add Product")
    print("4. View Products")
    print("5. Place Order")
    print("6. View Orders")
    print("7. Update Order Quantity")
    print("8. Delete Customer")
    print("9. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        add_customer(name, email)

    elif choice == "2":
        view_customers()

    elif choice == "3":
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        add_product(name, price)

    elif choice == "4":
        view_products()

    elif choice == "5":
        customer_id = input("Enter customer ID: ")
        product_id = input("Enter product ID: ")
        quantity = input("Enter quantity: ")
        add_order(customer_id, product_id, quantity)

    elif choice == "6":
        view_orders()

    elif choice == "7":
        order_id = input("Enter order ID: ")
        new_quantity = input("Enter new quantity: ")
        update_order_quantity(order_id, new_quantity)

    elif choice == "8":
        customer_id = input("Enter customer ID to delete: ")
        delete_customer(customer_id)


    elif choice == "9":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")