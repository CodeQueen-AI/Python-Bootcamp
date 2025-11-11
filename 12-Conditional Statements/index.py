# If Statements
age = 18
if age >= 18:
    print("You are eligible to vote!")
    
# If-Else
age = 16
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are NOT eligible to vote")


# If-elif-else
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# Nested If
age = 20

if age >= 18:
    print("You are an adult.")

    if age >= 21:
        print("You can also apply for driving license.")
    else:
        print("But you cannot apply for driving license yet.")
else:
    print("You are a minor.")
