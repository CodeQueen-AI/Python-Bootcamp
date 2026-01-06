Perfect! 😄 Maine aapke existing README ke saath ye **Classes in Python 🏫** section integrate kar diya hai. Yeh updated version hai:

---

# 🖥️ Object-Oriented Programming (OOP) in Python

## 📘 Introduction

Object-Oriented Programming (OOP) ek programming paradigm hai jisme hum real-world objects ko program ke andar model karte hain. OOP ka main focus **objects** aur **classes** par hota hai. Ye approach code ko organize karne, reuse karne aur maintain karne mein asaan banata hai.

**Key Features of OOP:**

* 🏷️ **Classes**: Templates ya blueprints jo objects banane ke liye use hoti hain.
* 🧩 **Objects**: Real instances of a class with actual data.
* ⚙️ **Methods**: Functions defined inside classes, jo objects ke data par operate karte hain.
* 🔑 **Encapsulation, Inheritance, Polymorphism, Abstraction**: OOP ke core principles.

---

## 🏫 Classes in Python

**Class kya hai?**
Class ek blueprint ya template hai jisse hum objects create karte hain. Ye real-world entities ko programming me represent karne ka tarika hai. ✨

**Class ke andar kya hota hai?**

* **Attributes (Variables) 📝:** Ye class ke andar data store karte hain. Har object ke apne attributes ho sakte hain.
* **Methods (Functions) ⚙️:** Ye class ke andar functions hote hain jo objects ke behavior ko define karte hain.
* **Constructor (`__init__`) 🚀:** Ye special method hai jo object create karte waqt automatically call hota hai aur attributes ko initialize karta hai.

**Object kya hai?**
Object class ka instance hota hai. Object ke paas class ke saare attributes aur methods available hote hain. 🧩

**Example:**

* Humne `Student` class banai jisme `name` aur `age` attributes hain.
* `show_info()` method se object ka data print hota hai.
* `s1 = Student("CodeQueen", 20)` → yeh ek object hai.
* `s1.show_info()` → object ka method call karte hain.

**Summary:**

* Class = blueprint 📘
* Object = class ka instance 🧩
* Attributes = object ka data 📝
* Methods = object ka behavior ⚙️
* Constructor = object create karte waqt initialize karne ke liye 🚀

---

## 🏗️ Classes in Python (Previous Section)

### 📌 What is a Class?

Class ek template hai jo objects ko define karta hai. Ye batata hai ki object ke paas kaunse **attributes (data)** aur **methods (actions)** honge.

#### 🔹 `self` Keyword

* `self` ek reference hai jo **current instance** ko represent karta hai.
* Iska use instance ke attributes aur methods ko access karne ke liye hota hai.
* Example: `self.first_name` ka matlab hai current patient instance ka first name.

---

## 🛠️ Methods in Classes

### 📌 What is a Method?

* Method ek function hai jo class ke andar define hota hai aur object ke data ko operate karta hai.
* Methods class ke behavior ko describe karte hain, jaise `say_if_minor()` method patient ka age check karta hai aur message print karta hai.

### 🔹 Features:

* `self` har method mein required hota hai, taake method instance ke attributes ko access kar sake.
* Methods ko objects ke upar call kiya jata hai: `pid346.say_if_minor()`

### ✏️ Changing Attributes with Methods

* Methods ka use karke hum object ke attributes ko update kar sakte hain.
* Example: `change_last_name()` method patient ka last name modify karta hai safely.

---

## 🔄 Instance vs Class Variables

### 🧩 Instance Variables

* Ye variables har object ke liye unique hote hain.
* Har instance apna alag copy rakhta hai.
* Defined **inside `__init__` constructor** using `self`.
* Example: `self.name`, `self.age`

### 🏥 Class Variables

* Ye variables **sab objects ke liye shared** hote hain.
* Class ke andar define kiye jate hain lekin `__init__` ke bahar.
* Example: `hospital_name = "City Hospital"`
* Sab instances is single copy ko use karte hain.

---

## ✅ Summary

* OOP real-world entities ko Python objects ke through model karta hai.
* **Classes** templates hain, **Objects** instances hain.
* **self** current object ko represent karta hai.
* **Methods** object ke behavior ko define karte hain.
* **Instance variables** unique data rakhte hain, **Class variables** shared data.
* OOP se code maintainable, reusable aur organized hota hai.

---

Agar chaho, mein is README ke liye **fully formatted GitHub ready Markdown file** bhi bana doon jisme emojis aur headings ke sath code snippets bhi highlight ho jaye.

Kya mein woh bana doon?
