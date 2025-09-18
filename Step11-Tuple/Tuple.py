#Tuple
my_tuple = (1, 2, 3, "apple", True)
print(my_tuple)

#Methods
# count()
my_tuple = (1, 2, 2, 3, 4, 2, 5)
print(my_tuple.count(2))

# index()
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple.index(30))

# len()
my_tuple = (10, 20, 30)
print(len(my_tuple))

# sorted()
my_tuple = (5, 3, 8, 1)
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple) 


# min()
my_tuple = (10, 20, 5, 40)
print(min(my_tuple)) 

# max()
print(max(my_tuple)) 

# sum()
my_tuple = (10, 20, 30)
print(sum(my_tuple))  

#Accessing Elements
# Indexing
my_tuple = ("apple", "banana", "cherry", "date")
print(my_tuple[0])  
print(my_tuple[2])  

# Negative Indexing
print(my_tuple[-1])
print(my_tuple[-2])

# Slicing
my_tuple = ("apple", "banana", "cherry", "date", "elderberry")

print(my_tuple[1:4])  
print(my_tuple[:3])  
print(my_tuple[2:])  


#Tuple Operations
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple) 

# Single Element Handling
single_tuple = (5,)  
not_a_tuple = (5)   
print(type(single_tuple))
print(type(not_a_tuple))   

# Convert Tuple to List
my_tuple = (1, 2, 3)
my_list = list(my_tuple)  
my_list.append(4)        
print(my_list)   


#Tuple Types
# Empty Tuple
empty_tuple = ()
print(empty_tuple)

# Single Element Tuple
single_tuple = (5,)  
print(single_tuple)  

# Tuple with Multiple Elements
multi_tuple = (10, 20, 30)  
print(multi_tuple) 

# Tuple with Different Data Types
mixed_tuple = (1, "Hello", 3.14, True)  
print(mixed_tuple)  

# Nested Tuple
nested_tuple = (1, (2, 3), (4, 5, 6))  
print(nested_tuple)  

# Tuple With Duplicates
duplicate_tuple = (1, 2, 2, 3, 4, 4, 5)  
print(duplicate_tuple)  

# Tuple With Range
range_tuple = tuple(range(1, 6))  
print(range_tuple)


