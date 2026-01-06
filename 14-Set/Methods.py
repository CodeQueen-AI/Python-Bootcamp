# Add() → adds a single item to the set
fruits = {"Apple", "Banana"}
fruits.add("Grape")
print(fruits)

# Update() → adds multiple items to the set
fruits = {"apple", "banana"}
fruits.update(["mango", "orange", "grape"])
print(fruits)

# Remove() → removes a specific item (error if not found)
fruits = {"Apple", "Banana"}
fruits.remove("Banana")
print(fruits)

# Discard() → removes a specific item (no error if not found)
fruits = {"Apple", "Banana"}
fruits.discard("Banana")
print(fruits)

# Pop() → removes and returns a random item
fruits = {"Apple", "Banana", "Orange"}
fruits.pop()
print(fruits)

# Clear() → removes all items
fruits = {"Apple", "Banana"}
fruits.clear()
print(fruits)

# Copy() → makes a copy of the set
fruits = {"Apple", "Banana"}
new_fruits = fruits.copy()
print(new_fruits)

# isdisjoint() → checks if two sets have no common items
set1 = {"Apple", "Banana"}
set2 = {"Orange", "Pineapple"}
print(set1.isdisjoint(set2))  

# issubset() → checks if set1 is completely inside set2
set1 = {"Apple", "Banana"}
set2 = {"Apple", "Banana", "Orange"}
print(set1.issubset(set2)) 

# issuperset() → checks if set1 contains all items of set2
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Apple", "Banana"}
print(set1.issuperset(set2))  
