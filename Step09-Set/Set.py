# 1. Creating a Set
my_set = {1, 2, 3, 4}
print("Creating a Set:", my_set)

# -----------------------------
# 2. Accessing Elements
# -----------------------------
my_set = {"apple", "banana", "cherry"}
print("\nAccessing with Loop:")
for item in my_set:
    print(item)

print("Accessing with List Conversion:", list(my_set)[0])

# -----------------------------
# 3. Adding Elements
# -----------------------------
my_set = {1, 2}
my_set.add(3)       
my_set.update([4, 5])  
print("\nAfter Adding Elements:", my_set)

# -----------------------------
# 4. Removing Elements
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)       
my_set.discard(10)     
my_set.pop()         
print("\nAfter Removing Elements:", my_set)

my_set.clear()         # Remove all elements
print("After Clearing Set:", my_set)

# -----------------------------
# 5. Set Operations
# -----------------------------
a = {1, 2, 3}
b = {3, 4, 5}
print("\nUnion:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# -----------------------------
# 6. Membership Test
# -----------------------------
my_set = {"apple", "banana", "cherry"}
print("\nMembership Test:")
print("apple in set?", "apple" in my_set)
print("mango not in set?", "mango" not in my_set)

# -----------------------------
# 7. Set Methods
# -----------------------------
a = {1, 2, 3}
b = {3, 4, 5}
print("\nSet Methods:")
print("Length of set a:", len(a))
print("Copy of set a:", a.copy())
print("a and b disjoint?", a.isdisjoint(b))
print("a is subset of {1,2,3,4}?", a.issubset({1, 2, 3, 4}))
print("{1,2,3,4} is superset of a?", {1, 2, 3, 4}.issuperset(a))

# -----------------------------
# 8. Frozen Set
# -----------------------------
my_frozen = frozenset([1, 2, 3])
print("\nFrozen Set:", my_frozen)
# my_frozen.add(4) ❌ Error (cannot modify)

my_frozenset = frozenset([1,2,3])
print(my_frozenset)

my_frozen_1 = frozenset([1,2,3,4,5,6,7,8])
fruit = frozenset(['apple'])