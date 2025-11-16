# Dunder (Magic) Methods in Python ✨

**Dunder Methods kya hai?**  
Dunder Methods, ya Magic Methods, special methods hote hain jinke names **double underscores** se start aur end hote hain, jaise `__init__`, `__str__`, `__add__`.  
Ye Python ke built-in behavior ko **customize** karne ke liye use hote hain. 🔮

**Dunder Methods kyun use karte hain?**  
- Objects ke behavior ko **customize** karne ke liye  
- Operators (+, -, *, ==, <, >) aur built-in functions (`len()`, `str()`) ke behavior ko redefine karne ke liye  
- Code ko **readable aur intuitive** banane ke liye  
- Real-world objects ke interactions ko **easily model** karne ke liye  

---

## 🔹 Common Dunder Methods

### 1️⃣ `__init__` 🚀  
- Constructor method  
- Object create hote hi automatically call hota hai  
- Object ke attributes ko initialize karne ke liye use hota hai  

### 2️⃣ `__str__` 🖊️  
- Object ka **human-readable representation** return karta hai  
- `print(object)` me ye automatically call hota hai  

### 3️⃣ `__len__` 📏  
- Object ka **length/size** return karta hai  
- `len(object)` call karne pe trigger hota hai  

### 4️⃣ `__add__` ➕  
- Operator `+` ka **custom behavior** define karne ke liye use hota hai  
- Object ke addition ko customize karte hain  

### 5️⃣ `__eq__`, `__lt__`, `__gt__` ⚖️  
- Comparison operators ka custom behavior define karte hain  
- `==`, `<`, `>` jaise operators objects ke liye work karte hain  

### 6️⃣ `__del__` 🗑️  
- Destructor method  
- Object delete hone par automatically call hota hai  

---

**Summary:**  
- Dunder Methods = **special methods with double underscores** ✨  
- Common methods = `__init__` 🚀, `__str__` 🖊️, `__len__` 📏, `__add__` ➕, `__eq__`/`__lt__`/`__gt__` ⚖️, `__del__` 🗑️  
- Benefits = **customized behavior, readable code, real-world modeling** 🔮
