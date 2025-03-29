import mysql.connector
import pandas as pd

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="newuser",
    password="112233445566",
    database="company_db"
)

cursor = conn.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM employees")

# Fetch column names
columns = [col[0] for col in cursor.description]
print(cursor.description)
# Fetch data and store in DataFrame
df = pd.DataFrame(cursor.fetchall(), columns=columns)

# Close connection
cursor.close()
conn.close()

# Display the DataFrame
print(df)