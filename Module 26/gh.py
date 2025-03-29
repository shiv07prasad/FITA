from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this if needed
    password="password",  # Change this if needed
    database="mydatabase"
)
cursor = db.cursor(dictionary=True)

# GET: Fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

# POST: Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    db.commit()
    return jsonify({"message": "User added successfully!"})

# PUT: Update a user
@app.route('/users', methods=['PUT'])
def update_user():
    data = request.json
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (data['name'], data['email'], data['id']))
    db.commit()
    return jsonify({"message": "User updated successfully!"})

# DELETE: Remove a user
@app.route('/users', methods=['DELETE'])
def delete_user():
    data = request.json
    cursor.execute("DELETE FROM users WHERE id=%s", (data['id'],))
    db.commit()
    return jsonify({"message": "User deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)