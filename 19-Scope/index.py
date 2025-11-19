# Local Scope
def my_func():
    x = 10  # local variable
    print(x)

my_func()
# print(x)  # ❌ Error, x is not defined outside


# Global Scope
y = 20  # global variable

def my_func():
    print(y)  # can access global variable

my_func()
print(y)  # also works outside
