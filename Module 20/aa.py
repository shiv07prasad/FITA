def something(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
print(something(nested))


