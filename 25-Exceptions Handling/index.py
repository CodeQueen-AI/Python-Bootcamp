# ⚠️ Python Exception Handling Example

# 1. Try / Except Block
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Please enter valid numbers.")

print("\n")

# 2. Try / Except / Else / Finally
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid input!")
else:
    print("No errors, input is valid.")
finally:
    print("This will always execute, whether error occurred or not.\n")

# 3. Raising Custom Exception
def check_age(age):
    if age < 18:
        raise Exception("Age must be at least 18!")
    else:
        print("Access granted.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except Exception as e:
    print("Error:", e)
