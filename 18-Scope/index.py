# Scope: The region of the code where a variable can be accessed

# Local Scope: variable that can only be accessed inside the function
def my_func():
    x = 10 
    print(x)

my_func()
# print(x)  # ❌ Error, x is not defined outside the function

# Global Scope: variable that can be accessed from anywhere in the program
y = 20 

def my_func():
    print(y)  # can access the global variable

my_func()
print(y)  # also works outside the function  
