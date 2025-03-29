students = {
    "101": {"name": "Alice", "age": 21, "grades": {"math": 90, "science": 85}},
    "102": {"name": "Bob", "age": 22, "grades": {"math": 80, "science": 88}},
}

# Accessing nested values
print(students["101"]["name"])        # Output: Alice
print(students["102"]["grades"]["math"])  # Output: 80
