#If Else
age = 16
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are NOT eligible to vote.")
    
#If Statement
age = 18
if age >= 18:
    print("You are eligible to vote!")
    
#If-elif-else
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")
    
#Nested if
num = 10
if num > 0:
    print("Positive Number")
if num % 2 == 0:
    print("Even Number")

age = 20  
if age >= 18: 
    print("You are eligible to vote.")  
if age >= 21:
    print("You are also eligible to apply for a driving license.")
    