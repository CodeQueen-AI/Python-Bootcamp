# Tuple
my_tuple = (1, 2, 3, 4)
print(my_tuple)

# Tuple to List
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print("List:", my_list) 

# List to Tuple
new_list = [5, 6, 7, 8]
new_tuple = tuple(new_list)
print("Tuple:", new_tuple) 

# Tuple Packing
my_tuple = 10, 20, 30, 40
print(my_tuple)  

# Tuple Unpacking
a, b, c, d = my_tuple
print("Unpacked Values:")
print(a) 
print(b)
print(c) 
print(d)

# Tuple Immutability
my_tuple = (1, 2, 3, 4)
try:
    my_tuple[1] = 10
except TypeError as e:
    print("Error:", e)