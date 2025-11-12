# 🧾 Dictionaries in Python

Dictionaries in Python are **unordered**, **changeable**, and **key-value pairs** based data structures. They are defined using curly braces `{}`.

# 📌 Python Dictionaries - README

A **Dictionary** Python mein ek aisi data structure hai jisme **keys** aur **values** ka combination hota hai. Ye values ko efficiently access karne, update karne aur organize karne ke liye use hoti hai. ✅

## Creating Dictionaries 🟢

* Normal dictionary using curly braces `{}`
* Using `dict()` constructor
* Keys unique hoti hain aur values kisi bhi type ki ho sakti hain

## Accessing Elements 🔢

* Elements ko **keys** ke through access karte hain
* `get()` function safer way hai, jisme default value bhi set kar sakte ho agar key na mile

## Dictionary Methods ➕

* **keys()** → dictionary ke saare keys return karta hai
* **values()** → dictionary ke saare values return karta hai
* **items()** → dictionary ke (key, value) pairs return karta hai
* **get(key)** → specific key ka value return karta hai, agar key nahi hai to None ya default value
* **update()** → dictionary me naye key-value pairs add ya existing values update karta hai
* **pop(key)** → specific key ka item remove karke value return karta hai
* **popitem()** → last inserted key-value pair remove karke return karta hai
* **clear()** → dictionary ke saare elements remove kar deta hai

## Nested Dictionaries 🥝

* Dictionary ke andar dusri dictionary ho sakti hai
* Access aur modify karne ke liye nested keys ka use karte hain
* Iteration ke liye nested loops use hote hain

## Iterating through Nested Dictionary 🔄

* Outer loop se student keys access karte hain
* Inner loop se unke key-value pairs iterate karte hain

## Why Use Dictionaries? 💡

* Keys se direct value access karna easy hai
* Efficient storage aur quick lookup possible hai
* Hierarchical data store karne ke liye nested dictionaries use hote hain
* Mutable (changeable) - add, remove aur modify karna possible hai
* Key-value pairs ka structure real-life scenarios me useful hota hai, jaise students info, product catalog, etc.
