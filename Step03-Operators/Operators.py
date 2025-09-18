# Arithematic Operators (+ , - , * , / , % , ** , //)
a = 10 + 5 
b = 10 - 5   
c = 10 * 5 
d = 10 / 2   
e = 10 % 3   
f = 10 ** 2  
g = 10 // 3  
print('Arithematic Operators :' , a, b , c, d, e, f, g)

# Assignment Opertaor (+= , -= , = , *= , /= , //=)
x = 10  
x += 5  
x -= 3  
x *= 2  
x /= 2  
x %= 4
x **= 3 
print(x)

#Comparison operators
x = 5 > 3  
print(x)
y = 5 < 3 
print(y)
z = 5 == 5 
print(z)
w = 5 != 3  
print(w)
p = 5 >= 5
print(p)
q = 5 <= 10 
print(q)


#Bitwise Operators
a = 5 & 3 
b = 5 | 3 
c = 5 ^ 3  
d = ~5    
e = 5 << 1 
f = 5 >> 1 
print(a, b, c, d, e, f)

#Identity Operators
a = [1, 2, 3]  
b = a  
print(a is b)     # True (Same object)
print(a is not b) # False (Not different objects)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True (Same values)
print(x is y)  # False (Different objects)


#Logical Operators
a = (5 > 3) and (10 > 5)  
print(a)

b = (5 > 10) or (10 > 5) 
print(b)

c = not(5 > 3)            
print(c)

#Memebership Operators
my_list = [1, 2, 3]
print(2 in my_list)   
print(5 not in my_list)

#Relational Operators
a = 10
b = 5

print(a == b)
print(a != b)  
print(a > b)  
print(a < b)  
print(a >= b)
print(a <= b)  