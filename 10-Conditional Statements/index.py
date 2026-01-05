# Conditional Stataments : Decides which code block runs based on conditions.

# If Statements : Checks only one condition
age = 18
if age >= 18:
    print("You are eligible to vote!")
    
# If-Else : Runs one block if a condition is true, otherwise runs another block
age = 16
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are NOT eligible to vote")

# If-elif-else : Checks multiple conditions; runs the first true block or else block
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Nested If : An if statement inside another if statement.
age = 20

if age >= 18:
    print("You are an adult.")

    if age >= 21:
        print("You can also apply for driving license.")
    else:
        print("But you cannot apply for driving license yet.")
else:
    print("You are a minor.")
