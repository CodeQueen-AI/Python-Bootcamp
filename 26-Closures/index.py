# Closures : A function that remembers values from its enclosing (outer) function even after the 
# outer function has finished executing
def outer():
    message = "Hello Code Queen"  

    def inner():
        return message         

    return inner               

my_closure = outer()
print(my_closure())


