import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="company_db"
)

cursor = conn.cursor()

employees = []  # List to store multiple employee records

while True:
    employee_id = int(input("Enter Employee ID: "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    hourly_pay = float(input("Enter Hourly Pay: "))
    hire_date = input("Enter Hire Date (YYYY-MM-DD): ")

    # Append employee data as a tuple
    employees.append((employee_id, first_name, last_name, hourly_pay, hire_date))

    more = input("Do you want to add another employee? (yes/no): ").strip().lower()
    if more != "yes":
        break
query = "INSERT INTO employees (employee_id, first_name, last_name, hourly_pay, hire_date) VALUES (%s, %s, %s, %s, %s)"
# Execute bulk insertion using executemany
cursor.executemany(query ,employees)
conn.commit()

print(f"{cursor.rowcount} employees inserted successfully!")

# Close connection
cursor.close()
conn.close()
