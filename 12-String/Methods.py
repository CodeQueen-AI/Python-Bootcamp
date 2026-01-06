# upper : makes text uppercase
text = 'CodeQueen'
print(text.upper())

# strip : removes extra spaces
text = '  CodeQueen  '
print(text.strip())

# replace : changes text
text = 'I love JS'
print(text.replace('JS', 'Python'))

# split : breaks string into list
text = 'apple,banana,orange'
print(text.split(','))

# join : joins list into string
words = ['I', 'Love', 'Python']
print(" ".join(words))

# find : finds position of text
text = "Hello Code Queen"
print(text.find("Code"))

# count : counts occurrences
text = "banana"
print(text.count("a"))

# capitalize : first letter uppercase
text = "hello world"
print(text.capitalize())

# swapcase : switches cases
text = "Hello Code Queen"
print(text.swapcase())

# isalpha : only letters
print("Hello".isalpha())

# isdigit :  only numbers
print("12345".isdigit())

# isalnum : letters and numbers
print("Python123".isalnum())