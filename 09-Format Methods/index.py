
# Format() Methods
name = 'CodeQueen'
age = 18
print('My name is {} and I am {} Years Old' .format(name, age))

# Using Index Numbers
print('My name is {0} and I am {1} Years Old.' .format(name, age))

# Using PlaceHolders
print('My Name is {n} and I am {a} Years Old.' .format(n=name, a=age))

# Expressions
a = 10
b = 3
print('The sum of {} and {} is {}' .format(a, b , a+b))
