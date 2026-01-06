# Higher-Order Function (HOF) : unction that can take another function as argument

from functools import reduce

# Function as Argument
def greet(name):
    """Simple function returning a greeting"""
    return f"Hello, {name}!"

def call_function(func, name):
    """Higher-order function: takes a function as argument"""
    print(func(name))

# Using custom HOF
call_function(greet, "Code Queen") 

# Function Returning a Function (Closure)
def outer_function(msg):
    """Returns another function"""
    def inner_function(name):
        return f"{msg}, {name}!"  
    return inner_function

my_greet = outer_function("Hi")
print(my_greet("Code Queen")) 

# Built-in HOFs: map, filter, reduce
nums = [1, 2, 3, 4, 5]

# map(): Apply function to every element
squared = list(map(lambda x: x**2, nums))  # square each number
print(squared)  # [1, 4, 9, 16, 25]

# filter(): Select elements based on a condition
evens = list(filter(lambda x: x % 2 == 0, nums))  # keep even numbers
print(evens)  # [2, 4]

# reduce(): Combine elements to a single value
sum_nums = reduce(lambda x, y: x + y, nums)  # sum of all numbers
print(sum_nums)  # 15