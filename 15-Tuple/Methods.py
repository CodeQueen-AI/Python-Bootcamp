# count() → counts how many times a value appears
my_tuple = (1, 2, 2, 3, 4, 2, 5)
print(my_tuple.count(2))  # 3

# index() → returns position of first occurrence of a value
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple.index(30))  # 2

# len() → counts number of items
my_tuple = (10, 20, 30)
print(len(my_tuple))  # 3

# sorted() → returns sorted list, convert back to tuple if needed
my_tuple = (5, 3, 8, 1)
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)  # (1, 3, 5, 8)

# min() → smallest value
my_tuple = (10, 20, 5, 40)
print(min(my_tuple))  # 5

# max() → largest value
print(max(my_tuple))  # 40

# sum() → sum of all items
my_tuple = (10, 20, 30)
print(sum(my_tuple))  # 60
