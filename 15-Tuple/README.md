# 📝 Tuples in Python

.

# 📌 Python Tuples - README

A **Tuple** Python mein ek aisi data structure hai jisme multiple values ko ek hi variable mein store kiya ja sakta hai. Tuple ke elements **immutable** hote hain, matlab unhe change nahi kiya ja sakta. ✅

## Creating Tuples 🟢

* Tum normal tuple create kar sakti ho: `(1, 2, 3)`
* Single element tuple banate waqt comma use karna zaroori hai: `(5,)`

## Converting between Tuple and List 🔄

* **Tuple to List**: `list(my_tuple)` → tuple ko list me convert karta hai.
* **List to Tuple**: `tuple(my_list)` → list ko tuple me convert karta hai.

## Tuple Packing and Unpacking ➕

* **Packing**: Multiple values ko ek tuple me store karna.
* **Unpacking**: Tuple ke elements ko alag-alag variables me assign karna.

## Immutability of Tuples ❌

* Tuples ke elements ko **modify, add, ya delete** nahi kiya ja sakta.
* Agar try karoge to Python **TypeError** throw karega.

## Indexing & Slicing 🔢

* Tuples ordered hote hain, isliye elements ko **index** se access kar sakte ho.
* Negative indexing aur slicing bhi possible hai.

## Tuple Methods and Functions 🛠️

* `count(x)` → count karta hai ke element kitni baar tuple me hai.
* `index(x)` → batata hai ke element ka index kya hai.
* `len()` → tuple ka length.
* `sorted()` → elements ko sort karke naya tuple return karta hai.
* `min()` → minimum value.
* `max()` → maximum value.
* `sum()` → sum of elements.

## Nested Tuples 🥝

* Tuple ke andar dusri tuple bhi ho sakti hai.
* Nested elements ko **indexing** se access kar sakte ho.
* Nested tuple iterate karne ke liye **loop aur isinstance()** use karna hota hai.

## Why Use Tuples? 💡

* Immutable → safe from accidental modification.
* Can hold multiple data types.
* Ordered → elements ko index se access kar sakte ho.
* Useful for returning multiple values from a function.
