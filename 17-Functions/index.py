# Calling function
def greet_user():
    print("Hello! Welcome to Python Functions")
greet_user() 

# Passing Information to Functions
def greet_user(name):
    print("Hello,", name)
greet_user("CodeQueen")

def add_numbers(first_number, second_number):
  total = first_number + second_number
  print(total)
add_numbers(2,3)

# Returning Value
def add_numbers(a, b):
    total = a + b
    return total  
result = add_numbers(5, 3)  
print("The sum is:", result)

# Nested and Inner Functions
def outer_function(text):
    def inner_function():
        print("Inner says:", text)
    inner_function() 
outer_function("Hello, Code Queen!")


