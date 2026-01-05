# PEDMAS : Parentheses → Exponents → Division → Multiplication → Addition → Subtraction
# In Python, it decides the order in which operations are performed

# Simple Addition & Multiplication
result = 2 + 3 * 4
print(result)  

result = (2 + 3) * 4
print(result)  

# Subtraction & Division
result = 20 - 4 / 2
print(result)  

result = (20 - 4) / 2
print(result)  

# Exponents + Addition/Subtraction
result = 2 + 3 ** 2 - 1
print(result)  

result = (2 + 3) ** 2 - 1
print(result)  

# Complex Expression
a, b, c, d, e = 1, 2, 3, 5, 8

# Without parentheses
final = a + b * c - d / e
print(final)

# With parentheses (clear)
final = (a + b) * (c - (d / e))
print(final)
