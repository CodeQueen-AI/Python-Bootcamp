# Loop: A block of code that repeats multiple times.

# For Loop: Repeats a block of code a specific number of times
for num in range(1, 6):
    print(num)  

# While Loop: Repeats a block of code as long as a condition is True
count = 1  
while count <= 5: 
    print(count)   
    count += 1    
    
# Nested Loop: A loop inside another loop
for i in range(1, 4):  
    for j in range(1, 4):  
        print(i, j)

# Control Statements: Statements that change the normal flow of a loop

# break: Exits the loop immediately
for num in range(1, 6):  
    if num == 3:  
        break     
    print(num)

# continue: Skips the current iteration and moves to the next one
for num in range(1, 6):
    if num == 3: 
        continue  
    print(num)

# pass: Does nothing, acts as a placeholder
for num in range(1, 6):
    if num == 3: 
        pass
    print(num)


# Example combining break, continue, and pass
# Loop through numbers 1 to 10
for num in range(1, 11):

    if num == 3:
        print("Continue applied: 3 is skipped")
        continue  # skips 3

    if num == 7:
        print("Pass applied: 7 does nothing (skipped silently)")
        pass  # does nothing

    if num == 9:
        print("Break applied: loop stops at 9")
        break  # exits the loop

    print("Number:", num)
