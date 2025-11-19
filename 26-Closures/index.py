def outer():
    message = "Hello Code Queen"  

    def inner():
        return message         

    return inner               

my_closure = outer()
print(my_closure())


