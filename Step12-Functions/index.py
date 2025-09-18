#1-Basic Functions

# Simple function
def greet():
    print("Hello, Code Queen!")
greet()

# Another basic function
def message():
    print('Hello I am CodeQueen, Future AI Engineer')

message()

#2-Functions with Parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Sumbal")

#3-Functions with Default Arguments
def greet_user(name="Code Queen"):
    print(f"Hello, {name}!")
greet_user()         
greet_user("Anusha")  


#4-Function Return Values
# No return
def greet():
    print("Hello, Code Queen!")

result = greet()
print(result)  

# Returning single value
def square(n):
    return n * n

print(square(5))

# Returning multiple values
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)

# Returning a list
def get_numbers():
    return [1, 2, 3, 4, 5]

print(get_numbers())

# Returning a dictionary
def get_student():
    return {"name": "CodeQueen", "age": 17}

print(get_student())

#5-Higher-Order Functions**
# Passing a function as argument
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x * x, 5)
print(result)

# Returning a function
def outer_function():
    def inner_function():
        return "Hello from Inner Function!"
    return inner_function

func = outer_function()
print(func())

# Returning a lambda function
def multiply_by(n):
    return lambda x: x * n

double = multiply_by(2)
print(double(5))

#6-Positional, Keyword, and Arbitrary Arguments
# Positional arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet("CodeQueen", 17)

# Keyword arguments
def info(name, age):
    print(f"Name: {name}, Age: {age}")

info(age=17, name="CodeQueen")

# Arbitrary positional arguments
def add_numbers(*numbers):
    total = sum(numbers)
    print(f"Sum: {total}")

add_numbers(2, 4, 6, 8)

# Arbitrary keyword arguments
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="CodeQueen", age=17, city="Karachi")

#7-Lambda (Anonymous) Functions
# Single parameter
square = lambda x: x * x
print(square(5))

# Multiple parameters
add = lambda x, y: x + y
print(add(3, 7))

# Using lambda with map & filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#8-Function Scope
# Function scope
def example():
    x = 10
    print(x)

example()
# print(x)  # Error, x is local

# Block scope
if True:
    y = 20
print(y)  # Works in Python (no block-level scope)


#9-Built-in Functions with Functions
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# reduce() sum
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)

# reduce() max
numbers = [10, 5, 30, 20]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)

# zip() and unzip
names = ["CodeQueen", "Anusha", "Ifra"]
scores = [95, 88, 76]
combined = list(zip(names, scores))
print(combined)

names, scores = zip(*combined)
print(names)
print(scores)

# sorted()
numbers = [5, 2, 9, 1, 5, 6]
print(sorted(numbers))                
print(sorted(numbers, reverse=True)) 
words = ["banana", "apple", "cherry", "kiwi"]
print(sorted(words, key=len))         

# enumerate()
names = ["CodeQueen", "Anu", "Ifra"]
for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")


#10-Special Functions (Object-Oriented)
# Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("CodeQueen", 17)
print(person1.name, person1.age)

# __str__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person1 = Person("CodeQueen", 17)
print(person1)

# __len__ & __getitem__
class Numbers:
    def __init__(self, nums):
        self.nums = nums

    def __len__(self):
        return len(self.nums)

    def __getitem__(self, index):
        return self.nums[index]

numbers = Numbers([10, 20, 30])
print(len(numbers))
print(numbers[1])

