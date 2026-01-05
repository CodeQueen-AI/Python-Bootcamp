# Logical Operators: Combine or reverse Boolean values (True/False)
a = (5 > 3) and (10 > 5)  # AND: True if both conditions are True → True
print(a)

b = (5 > 10) or (10 > 5)  # OR: True if at least one condition is True → True
print(b)

c = not(5 > 3)            # NOT: Reverses the result → False
print(c)