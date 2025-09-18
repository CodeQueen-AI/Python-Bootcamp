#for loop
for i in range(1, 6):   
    print(i)

#while loop
i = 1
while i <= 5:
    print(i)
    i += 1  
    
#break statement
for i in range(1, 10):
    if i == 5:
        break   
    print(i)

#Continue Statement
for i in range(1, 6):
    if i == 3:
        continue   
    print(i)

#pass statement
for i in range(1, 6):
    if i == 3:
        pass  
    print(i)
    
#Nested Loop
for i in range(1, 4):  
    for j in range(1, 4):  
        print(f"{i} x {j} = {i*j}")  
    print("------")  

#Iteration in Python Loop
#String Iteration
for data in "Python":
    print(data)

#List Iteration
for item in ["Apple", "Banana", "Cherry"]:
    print(item)

# Tuple Iteration
for num in (10, 20, 30):
    print(num)

#Dictionary Iteration
for key, value in {"name": "Ali", "age": 20}.items():
    print(key, value)

# Set Iteration
for num in {5, 10, 15}:
    print(num)
    

#Loop with Else Statement
for num in range(1, 6):  
    print(num)  
else:  
    print("Loop completed successfully!")  

#Loop with Break
for num in range(1, 6):  
    if num == 3:  
        break  
    print(num)  
else:  
    print("Loop completed!") 
    
    
