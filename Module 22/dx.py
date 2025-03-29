import re

import re

text = "Name: Jaa Daaa dgvdgvsdvhcv  Name: Saaa Kaaa hbhjdshvv Name: gfgfgfgfgf hghghghg ioioio"
pattern = r"Name: (\w+) (\w+) (\w+)"

matches = re.findall(pattern, text)

for one,two ,three in matches:
    print("First Name:", one)
    print("Middle Name:",two)
    print("Last Name:", three)
    print("---")
