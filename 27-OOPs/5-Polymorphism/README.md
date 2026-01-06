# Polymorphism in Python 🔄

**Polymorphism kya hai?**  
Polymorphism OOP ka concept hai jisme **same function ya operator ka different behavior** hota hai objects ke context ke hisaab se.  
Ye program ko flexible aur reusable banata hai. ✨

**Polymorphism kyun use karte hain?**  
- Same function name ya operator ka **different behavior** allow karne ke liye  
- Code ko **flexible aur organized** banane ke liye  
- Complex systems me **different objects ke liye similar interface** provide karne ke liye  

---

## 🔹 Types of Polymorphism

### 1️⃣ Compile-time Polymorphism (Static Polymorphism) ⚡  
- Ye **function overloading** ke through achieve hota hai  
- Python me strictly function overloading nahi hoti, lekin default arguments ya multiple methods se simulate kiya ja sakta hai  
- Compile-time me decide hota hai ke **kaunsa method call hoga**  

### 2️⃣ Run-time Polymorphism 🏃‍♀️  
- Ye **method overriding** ke through achieve hota hai  
- Child class apne **parent class ke method ko override** kar sakti hai  
- Run-time me decide hota hai ke **kaunsa method execute hoga**  



## 🔹 Operator Overloading ➕➖✖️➗  

**Operator Overloading kya hai?**  
- Operators (+, -, *, ==, <, >, etc.) ka **custom behavior** objects ke liye define karna  
- Python me **Dunder (Magic) Methods** ka use hota hai, jaise `__add__`, `__sub__`, `__eq__`, `__lt__`, `__gt__`  

**Operator Overloading kyun use karte hain?**  
- Objects ke arithmetic aur comparison ko **customize** karne ke liye  
- Code ko **readable aur intuitive** banane ke liye  
- Real-world modeling me objects ke interactions ko easily define karne ke liye  



**Summary:**  
- Polymorphism = **same name, different behavior** 🔄  
- Types = Compile-time ⚡, Run-time 🏃‍♀️  
- Operator Overloading = **custom operators** ➕➖✖️➗  
- Benefits = **flexible, reusable aur readable code** ✨
