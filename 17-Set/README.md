# 🧾 Sets in Python

Sets in Python are unordered, mutable (except frozensets), and do not allow duplicate elements. They are defined using curly braces {}


A **Set** Python mein ek aisi data structure hai jo unique elements store karti hai. Set me order maintain nahi hota aur duplicate values automatically remove ho jaati hain. ✅

## Creating Sets 🟢

* Normal set: `fruits = {"Apple", "Banana", "Cherry"}`
* From a list: `unique_set = set([1, 2, 2, 3, 4])`
* From a string: `char_set = set("hello")`

## Accessing Elements 🔢

* Sets me indexing nahi hoti.
* Iteration ke liye **for loop** use hota hai.

## Frozen Sets ❄️

* Immutable sets ko **frozenset()** se create kiya jata hai.
* Frozen set me elements change nahi kiye ja sakte.

## Set Methods ➕

* **add()**: Single element add karta hai.
* **update()**: Multiple elements add karta hai.
* **remove()**: Specific element remove karta hai, agar element na ho to error deta hai.
* **discard()**: Specific element remove karta hai, error nahi deta agar element na ho.
* **pop()**: Random element remove karta hai aur return karta hai.
* **clear()**: Set ke saare elements remove karta hai.
* **copy()**: Set ki copy create karta hai.

## Set Checking Methods ✅

* **isdisjoint()**: Check karta hai ke do sets me common element nahi hai.
* **issubset()**: Check karta hai ke set1, set2 ka subset hai.
* **issuperset()**: Check karta hai ke set1, set2 ka superset hai.

## Set Operations 🔄

* **union()**: Dono sets ke unique elements ka combination.
* **intersection()**: Dono sets ke common elements.
* **difference()**: Set1 me jo elements set2 me nahi hain.
* **symmetric_difference()**: Jo elements dono sets me sirf ek me hain.

## Iterating Through a Set 🔁

* Set me **for loop** se iterate kar sakte hain.
* Indexing available nahi hai.

## Why Use Sets? 💡

* Unique elements store karna easy hai.
* Fast membership testing.
* Useful for mathematical operations like union, intersection, difference, and symmetric difference.
* Duplicate elements automatically remove ho jaate hain.
