def something(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
final_dict = something(dict1, dict2)
print(final_dict)
