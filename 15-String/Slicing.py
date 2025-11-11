text = "Programming"

# Basic Slicing [start:end] → extracts characters from start to end-1
print(text[0:5])  
print(text[3:8]) 

# 2️⃣ Slicing from start to a position [:end]
print(text[:6]) 

# 3️⃣ Slicing from a position to the end [start:]
print(text[5:])  

# 4️⃣ Negative Indexing with Slicing
print(text[-5:]) 
print(text[-10:-5])  

# 5️⃣ Slicing with Step [start:end:step]
print(text[0:10:2]) 
print(text[::3])   

# 6️⃣ Reverse a String using Slicing
print(text[::-1])  
