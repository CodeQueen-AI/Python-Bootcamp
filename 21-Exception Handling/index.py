# Exception Handling: Handling errors without crashing the program

# try : Block of code where you write code that might cause an error
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
# except : Block of code that runs if an error occurs in the try block
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")