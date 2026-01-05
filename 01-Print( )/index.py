# Print()
print('Hello World!')
print('Welcome to CodeQueen Python Repository!')

# Print Parameters

# end
print("Python", end=" ")
print("is fun")

# sep
print("Python", "is", "fun", sep="-")
print("2025", "10", "28", sep="/")

# flush
import time
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)