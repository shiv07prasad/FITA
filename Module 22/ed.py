import re

text = "Hello, welcome to Python Python regex!"
pattern = r"Python"

match = re.search(pattern, text)
if match:
    print("Pattern found at index:", match.start())  # Start index of the match
else:
    print("Pattern not found.")


import re

text = "Python is fun, and learning Python is even more fun!"
pattern = r"Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(f"Pattern found at index: {match.start()} to {match.end()-1}")

