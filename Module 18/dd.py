from collections import OrderedDict

od = OrderedDict(a=1, b=2, c=3, d=4)

# Keys to remove
keys_to_remove = ["b", "c"]

# Remove each key
for key in keys_to_remove:
    del od[key]

print(od)  # Output: OrderedDict([('a', 1), ('d', 4)])









