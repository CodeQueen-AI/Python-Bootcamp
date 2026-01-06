# Open a files
file = open("example.txt", "w")   
file.write("Welcome to Python File Handling!")
file.close()   

# Reading files
file = open("example.txt", "r")   
print("---- Full Content using read() ----")
print(file.read())               
file.close()

# Read one line
file = open("example.txt", "r")
print("---- One Line using readline() ----")
print(file.readline())            
file.close()

# Reads all lines into a list
file = open("example.txt", "r")
print("---- All Lines as List using readlines() ----")
print(file.readlines())           
file.close()

# Writing multiple lines (write, writelines)
file = open("example.txt", "w")
file.write("This is line 1.\n")
file.write("This is line 2.\n")
file.writelines(["This is line 3.\n", "This is line 4.\n"])
file.close()

# Appending data
file = open("example.txt", "a")  
file.write("This line was added later using append.\n")
file.close()

# Using 'with open()'
with open("example.txt", "r") as file:
    print("---- Using with open() ----")
    content = file.read()
    print(content)

# File paths

# Relative path (file in same folder)
with open("example.txt", "r") as file:
    print("---- Relative Path ----")
    print(file.read())

# Absolute path example (use your real path if needed)
with open("C:/Users/CodeQueen/Desktop/example.txt", "r") as file:
    print("---- Absolute Path ----")
    print(file.read())

# Handling file errors with try...except
try:
    with open("not_exist.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("⚠️ File not found! Please check the name or path.")

