import requests
BASE_URL = "http://127.0.0.1:5000/users"
response = requests.get(BASE_URL)
print(response.json())


### **2. Add a User**

response = requests.post(BASE_URL, json={"name": "Alice", "email": "alice@example.com"})
print(response.json())


### **3. Update a User**

response = requests.put(f"{BASE_URL}", json={"name": "Bob", "email": "bob@example.com","id":2})
print(response.json())


## **4. Delete a User**

# response = requests.delete(f"{BASE_URL}", json={"id":5})
# print(response.json())
