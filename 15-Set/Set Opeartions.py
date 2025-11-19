# Union()
set1 = {"Apple", "Banana"}
set2 = {"Orange", "Pineapple"}
new_set = set1.union(set2)
print(new_set)

# Intersection()
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
common = set1.intersection(set2)
print(common)

# Difference()
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
diff = set1.difference(set2)
print(diff)

# Symmetric Difference()
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)
