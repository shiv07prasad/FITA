import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()  # Converts JSON response into a Python dictionary

print(response.text)

print(data)  # Now 'data' is a Python list of dictionaries
