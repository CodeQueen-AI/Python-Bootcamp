# upper()
text = 'CodeQueen'
print(text.upper())

# strip
text = '  CodeQueen  '
print(text.strip())

# replace
text = 'I love JS'
print(text.replace('JS', 'Python'))

# split
text = 'apple,banana,orange'
fruits = text.split(',')
print(fruits)

# Join
words = ['I' , 'Love' , 'Python']
sentence = " ".join(words)
print(sentence)

# find
text = "Hello Code Queen"
print(text.find("Code"))  

# count(substring)
text = "banana"
print(text.count("a"))  

# capitalize
text = "hello world"
print(text.capitalize())  

# swapcase()
text = "Hello Code Queen"
print(text.swapcase())  

# #isalpha()
text = "Hello"
print(text.isalpha())

text = "Hello123"
print(text.isalpha())  

#isdigit()
text = "12345"
print(text.isdigit()) 

text = "123abc"
print(text.isdigit())  

#isalnum()
text = "Python123"
print(text.isalnum())  

text = "Python 123"
print(text.isalnum()) 
