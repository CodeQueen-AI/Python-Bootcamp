# 🔄 Type Casting in Python

**Type Casting:** Changing a value from **one data type to another**

In Python, type casting happens in **two ways**:


## 1️⃣ Implicit Type Casting

**(Automatic — done by Python)**

* Python **automatically converts** a data type when needed
* Happens when **smaller type + larger type** are used together, e.g., integer + float
* The programmer does **not need to do anything**

**Key Points:**

* Happens **without errors**
* Ensures **accurate results**
* Python decides the **best type**

**Example Situations:**

* `int + float` → int becomes float
* `bool + int` → bool becomes int



## 2️⃣ Explicit Type Casting

**(Manual — done by developer)**

* The programmer **forces Python to convert** a value to another type
* Used when Python **cannot automatically convert**

**Most Common Conversions:**

* Convert to integer
* Convert to float/decimal
* Convert to string
* Convert to boolean

**Key Points:**

* Done **manually** by programmer
* Errors can occur if conversion is **not possible**
* Gives **full control** to the programmer


## 🌟 Key Differences

| Feature    | Implicit Type Casting | Explicit Type Casting           |
| ---------- | --------------------- | ------------------------------- |
| Conversion | Automatic             | Manual by programmer            |
| Error Risk | Low                   | High if conversion not possible |
| Control    | Python decides        | Programmer decides              |



### ✅ Final Tip

* Use **explicit type casting** when Python cannot convert automatically
* Trust **implicit type casting** when Python can handle it safely