# Print() : its used to show something on the screen
print('Hello World!')
print('Welcome to CodeQueen Python Repository!')

# Print Parameters

# end : symbol between values
print("Python", end=" ")
print("is fun")

# sep : line ending
print("Python", "is", "fun", sep="-")
print("2025", "10", "28", sep="/")

# flush : show immediately or delay
import time
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)