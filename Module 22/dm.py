import re

pattern = r"\b\d{5}\b|cat"
text = "I love my dog and my cat. 12345"

matches = re.findall(pattern, text)
print(matches)  # Output: ['dog', 'cat']


pattern = r"(ab)+"
text = "abab ab abababa hgtsgababaabkdldld"

matches = re.findall(pattern, text)
print(matches)  # Output: ['ab', 'ab', 'ab']