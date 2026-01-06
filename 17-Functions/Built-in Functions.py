from functools import reduce

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 4, 5, 6]

# map() — Apply function to all items
squared = list(map(lambda x: x**2, numbers1))
print("map() — Squared numbers:", squared) 

# filter() — Filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers2))
print("filter() — Even numbers:", evens)  

# reduce() — Reduce items to a single value
total = reduce(lambda x, y: x + y, numbers1)
print("reduce() — Sum of numbers:", total)  
