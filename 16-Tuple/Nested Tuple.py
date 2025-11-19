nested_tuple = (1, 2, (3, 4, 5), 6)

# Accessing Elements
print(nested_tuple[0])     
print(nested_tuple[2])     
print(nested_tuple[2][1]) 

# Iterating through nested tuple
for item in nested_tuple:
    if isinstance(item, tuple):
        for sub_item in item:
            print(sub_item)
    else:
        print(item)
