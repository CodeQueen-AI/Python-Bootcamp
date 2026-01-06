# 🧾 Functions in Python

Functions in Python are **blocks of reusable code** that perform a specific task. They help organize code, avoid repetition, and make programs modular.

# 📌 Python Functions - README

A **Function** Python mein ek reusable code block hai jo **specific task** perform karta hai. Tum functions ko **define** aur **call** karte ho, aur ye values return bhi kar sakte hain✅

## Function Definition and Calling 

* Function define karte hain `def` keyword ke saath.
* Function ko call karne ke liye sirf uska name aur parentheses use karte hain.

## Passing Information to Functions 🔢

* Functions parameters accept kar sakte hain jo values function ke andar bhejte hain.
* Ye parameters positional ya keyword arguments ho sakte hain.

## Returning Values 🔄

* Functions values ko `return` keyword ke through return kar sakte hain.
* Returned value ko store kar ke use kiya ja sakta hai.

## Nested and Inner Functions 

* Ek function ke andar dusra function define kiya ja sakta hai.
* Inner function sirf outer function ke andar call hota hai.

## Higher-order Functions 🧮

* **Function taking another function as argument**: ek function ko argument ke tor pe use kar sakte hain.
* **Function returning another function**: ek function dusre function ko return kar sakta hai.

## Function Parameters ➕

### Positional Arguments

* Arguments order me diye jate hain.
* Example: `func(a, b)`

### Keyword Arguments

* Arguments explicitly key ke sath diye jate hain.
* Order important nahi.

### Default Arguments

* Parameters ke liye default values set ki ja sakti hain.
* Agar call me value na di jaye to default use hoti hai.

### Arbitrary Arguments (*args)

* Multiple positional arguments pass karne ke liye use hota hai.
* Function ke andar ye tuple ki tarah behave karta hai.

### Arbitrary Keyword Arguments (**kwargs)

* Multiple keyword arguments pass karne ke liye use hota hai.
* Function ke andar ye dictionary ki tarah behave karta hai.

### Mixing Arguments

* Positional, keyword, *args, aur **kwargs ko ek sath use kiya ja sakta hai.
* Syntax order important hai: positional → keyword → *args → **kwargs

## Built-in Higher-order Functions 📌

* **map()** → Function ko list ke har element pe apply karta hai.
* **filter()** → Condition ke basis pe elements filter karta hai.
* **reduce()** → List ke elements ko single value me reduce karta hai.

## Lambda Functions ⚡

* Anonymous functions jo ek line me define hote hain.
* Useful for short, simple operations.

## Recursive Functions 🔁

* Function jo khud ko call karta hai.
* Base condition define karna zaroori hai, warna infinite recursion ho sakti hai.
* Example: Factorial calculation.

## Type Hints 📝

* Functions me parameters aur return type ke liye hints add kar sakte hain.
* Code readability aur debugging me helpful hai.

## Why Use Functions? 💡

* Code reuse aur modularity easy hoti hai.
* Readability aur maintainability improve hoti hai.
* Complex programs ko manageable parts me divide kiya ja sakta hai.
* Higher-order aur nested functions se advanced functionalities implement karna possible hota hai.
