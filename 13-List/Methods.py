# Append() → adds an item at the end
fruits = ["apple", "banana"]
fruits.append("grapes")
print(fruits)

# Insert() → adds an item at a specific position
fruits = ["apple", "banana"]
fruits.insert(1, "watermelon")
print(fruits)

# Remove() → removes a specific item by value
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# Pop() → removes item by index (default last)
fruits = ["apple", "banana", "cherry"]
fruits.pop()    # removes last
print(fruits)
fruits.pop(0)   # removes first
print(fruits)

# Sort() → sorts items ascending
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

# Reverse() → reverses the order
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)

# Index() → finds position of an item
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))

# Count() → counts how many times an item appears
numbers = [1, 2, 3, 2, 2, 4]
print(numbers.count(2))

# Extend() → adds multiple items from another list
fruits = ["apple", "banana"]
more_fruits = ["watermelon", "grapes"]
fruits.extend(more_fruits)
print(fruits)

# Clear() → removes all items
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)

# Copy() → makes a new copy of the list
fruits = ["apple", "banana", "grapes"]
new_fruits = fruits.copy()
new_fruits.append("watermelon")
print("Original List:", fruits)
print("Copied List:", new_fruits)

# Sort(reverse=True) → sorts descending
numbers = [5, 2, 8, 1, 4]
numbers.sort(reverse=True)
print(numbers)

# del() → deletes item by index or entire list
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)

numbers = [1, 2, 3, 4]
del numbers  # deletes entire list
