# Add()
fruits = {"Apple", "Banana"}
fruits.add("Grape")
print(fruits)

# Update()
fruits = {"apple", "banana"}
fruits.update(["mango", "orange", "grape"])
print(fruits)

# Remove()
fruits = {"Apple", "Banana"}
fruits.remove("Banana")
print(fruits)

# Discard
fruits = {"Apple", "Banana"}
fruits.discard("Banana") 
print(fruits)

# Pop()
fruits = {"Apple", "Banana", "Orange"}
fruits.pop()
print(fruits)

# Clear()
fruits = {"Apple", "Banana"}
fruits.clear()
print(fruits)


# Copy()
fruits = {"Apple", "Banana"}
new_fruits = fruits.copy()
print(new_fruits)

# isdisjoint()
set1 = {"Apple", "Banana"}
set2 = {"Orange", "Pineapple"}
print(set1.isdisjoint(set2))

# issubset()
set1 = {"Apple", "Banana"}
set2 = {"Apple", "Banana", "Orange"}
print(set1.issubset(set2))

# issuperset()
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Apple", "Banana"}
print(set1.issuperset(set2))
