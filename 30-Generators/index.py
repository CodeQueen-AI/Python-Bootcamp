# Generator function
def my_generator():
    yield 1
    yield 2
    yield 3

# Creating generator object
gen = my_generator()

# Using generator
print(next(gen))  
print(next(gen))  
print(next(gen))  



def numbers():
    for i in range(1, 6):
        yield i  
gen = numbers()
print("Using loop to get all values:")
for n in gen:
    print(n)
