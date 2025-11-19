# 🌀 Abstraction in Python

## 🤔 What is Abstraction?

Abstraction ek **Object-Oriented Programming (OOP) concept** hai jiska maksad **complexity ko hide karna aur sirf essential features dikhana** hota hai.
Iska matlab hai ke user ko **unnecessary details nahi dikhaye jate**, sirf **important functionalities** available hoti hain.

**✨ Why use Abstraction?**

* Code ko **readable aur maintainable** banata hai 📝
* User ko **sirf zaroori operations** dikhata hai 🛠️
* Different classes ke liye **common interface** provide karta hai 🔗



## 🏛️ Abstract Classes

**Definition:**
Abstract Class ek aisi class hoti hai jo **sirf blueprint ka kaam karti hai**.
➡️ **Direct object nahi banate**.
Ye classes **abstract methods** define karti hain jinka implementation **derived (child) classes** me hota hai.

**Key Points:**

* Abstract class **object banane ke liye nahi**, sirf blueprint ke liye hoti hai 📐
* Iske andar **abstract methods** aur **normal methods** dono ho sakte hain ⚙️
* Har derived class ko **abstract methods ka implementation provide karna zaroori hai** ✅

**Why use Abstract Classes?**

* Common features define karne ke liye jo multiple classes share kar sakti hain 🔄
* Code ko **structured aur reusable** banata hai 🏗️



## ✨ Abstract Methods

**Definition:**
Abstract Method ek method hai jo **sirf declare ki jati hai**, aur iska **implementation child class me define hota hai**.
Ye method sirf **abstract class ke andar exist kar sakti hai**.

**Key Points:**

* Abstract method **sirf prototype** hoti hai, koi functionality nahi hoti 📝
* Child class me implement karna **mandatory** hota hai ✅
* Ye ensure karta hai ke **har derived class apna specific behavior define kare** 🎯

**Why use Abstract Methods?**

* Code ko **flexible aur scalable** banata hai 🌱
* Different classes ke liye **consistent interface** ensure karta hai 🔗





**📝 Summary:**

* **Abstraction** = unnecessary details hide karna, sirf essential dikhana 🕵️‍♀️
* **Abstract Class** = blueprint class, object nahi banate 🏛️
* **Abstract Method** = sirf declare ki method, implementation child class me ⚡
* Abstraction Python me **`ABC` module aur `abstractmethod` decorator** ke through implement hota hai 🐍
