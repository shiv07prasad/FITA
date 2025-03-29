import re

text = "Name: John Doe"
pattern = r"Name: (\w+) (\w+)"

match = re.search(pattern, text)
if match:
    print("First Name:", match.group(1))  # Output: First Name: John
    print("Last Name:", match.group(2))   # Output: Last Name: Doe