# break
for num in range(1, 6):  
    if num == 3:  
        break     
    print(num)

# continue
for num in range(1, 6):
    if num == 3: 
        continue  
    print(num)

# pass
for num in range(1, 6):
    if num == 3: 
        pass
    print(num)


# Loop through numbers 1 to 10
for num in range(1, 11):

    if num == 3:
        print("Continue laga: 3 skip hogaya")
        continue

    if num == 7:
        print("Pass laga: 7 pe kuch nahi hoga (skip silently)")
        pass 

    if num == 9:
        print("Break laga: 9 pe loop ruk jayega")
        break  

    print("Number:", num)