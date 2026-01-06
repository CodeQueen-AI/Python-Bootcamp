# Union() → combines all items from both sets (no duplicates)
set1 = {"Apple", "Banana"}
set2 = {"Orange", "Pineapple"}
new_set = set1.union(set2)
print(new_set)

# Intersection() → items common to both sets
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
common = set1.intersection(set2)
print(common)

# Difference() → items in set1 but not in set2
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
diff = set1.difference(set2)
print(diff)

# Symmetric Difference() → items in either set, but not in both
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)
