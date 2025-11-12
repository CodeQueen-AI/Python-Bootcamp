# Function Taking Another Function as Argument
def greet(name):
    return f"Hello, {name}!"

def call_function(func, name):
    print(func(name)) 

call_function(greet, "Sumbal")


# Function Returning Another Function
def outer_function(msg):
    def inner_function(name):
        return f"{msg}, {name}!"
    return inner_function

my_greet = outer_function("Hi")
print(my_greet("Code Queen"))