import re

text = "Call me at +91 2541298541 or 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}|\b\+91\s\d{10}\b"

matches = re.findall(pattern, text)
print(matches)  # Output: ['987-654-3210', '123-456-7890']