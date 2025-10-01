# Python Sets and Frozensets 🔗✨

**Definition:**  
A set in Python is an unordered collection of unique elements.  
A frozenset is an immutable version of a set, meaning it cannot be changed after creation.


## 1. Creating a Set 🛠️
- Use curly braces `{}` or the `set()` function.  
- Elements must be unique; duplicates are automatically removed.  


## 2. Accessing Elements 🔎
- Sets are unordered, so indexing is not possible.  
- Elements can be accessed by looping or converting the set into a list.  

## 3. Adding Elements ➕
- **add()** → Add a single element.  
- **update()** → Add multiple elements.  


## 4. Removing Elements ❌
- **remove()** → Remove a specific element; raises an error if not found.  
- **discard()** → Remove a specific element; does not raise an error if not found.  
- **pop()** → Remove and return a random element.  
- **clear()** → Remove all elements.  


## 5. Set Operations ⚡
- **Union (|)** → Combines elements from two sets.  
- **Intersection (&)** → Elements common to both sets.  
- **Difference (-)** → Elements in one set but not in the other.  
- **Symmetric Difference (^)** → Elements in either set, but not in both.  


## 6. Membership Test 🔐
- **in** → Check if an element exists in the set.  
- **not in** → Check if an element does not exist in the set.  

## 7. Set Methods 🧰
- **len()** → Number of elements in the set.  
- **copy()** → Returns a shallow copy of the set.  
- **isdisjoint()** → Returns True if two sets have no elements in common.  
- **issubset()** → Checks if a set is a subset of another.  
- **issuperset()** → Checks if a set contains all elements of another.  



## 8. Frozenset ❄️
- An immutable set that cannot be modified.  
- Useful when a set needs to remain constant or be used as a dictionary key.  


