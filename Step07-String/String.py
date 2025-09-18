#String
name = "Code Queen"
print(name)

#Methods
#Uppercase()
txt = "hello"
print(txt.upper())   

#Lowercase()
txt = "HELLO"
print(txt.lower())   

#Stripe()
txt = "  Python  "
print(txt.strip())   

#Replace()
txt = "I like Java"
print(txt.replace("Java", "Python"))   

#Split()
txt = "Apple, Banana, Cherry"
print(txt.split(", "))   

#Find()
txt = "Python"
print(txt.find("t"))  

#Len()
txt = "CodeQueen"
print(len(txt))  

#Single Quotes
single_quote = 'Single Quotes'
print(single_quote)

#Double Quotes
double_quote = "Double Quotes"
print(double_quote)

#Triple Quotes
multi_line = """
Triple
Quotes
"""
print(multi_line)

#String Manipulation
#String Slicing  
text = "Programming"
print(text[0:5])   
print(text[-5:]) 

# String Concatenation 
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  

#String Repetition (*)
text = "Python"
print(text * 3)  

#String Splitting & 
text = "Hello,World,Python!"
words = text.split(",") 
print(words)

#String Joining
words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence)
 
#string Formatting
name = "Code Queen"
age = 17
print(f"My name is {name} and I am {age} years old")  

text = "Python"
# Positive Indexing
print("Positive Indexing")
print(text[0])  
print(text[2]) 
print(text[5])  

# Negative Indexing
print("\nNegative Indexing")
print(text[-1]) 
print(text[-3]) 
print(text[-6])

