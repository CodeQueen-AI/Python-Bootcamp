# Decorators in Python 🎀
**Decorators kya hai?**  
Decorators ek special tool hai jisse hum **methods ya functions ko modify ya enhance** kar sakte hain bina unke original code ko change kiye.  
Ye OOP aur functions ke behavior ko flexible aur reusable banata hai. ✨

**Decorators kyun use karte hain?**  
- Methods ke behavior ko **enhance ya modify** karne ke liye  
- Code ko **clean aur maintainable** banane ke liye  
- Repetitive code avoid karne ke liye  


## 🔹 Common Decorators in Classes

### 1️⃣ @classmethod 🏛️  
- Class level method banata hai  
- `cls` parameter ka use hota hai  
- Object create kiye bina bhi call kiya ja sakta hai  

**Use:**  
- Class variables ko access ya modify karne ke liye  
- Factory methods create karne ke liye  



### 2️⃣ @staticmethod 🛠️  
- Class ke andar independent method banata hai  
- Na `self`, na `cls` parameter required  
- Object ya class dono se call ho sakta hai  

**Use:**  
- Independent utility functions ya helpers ke liye  



### 3️⃣ @property 💠  
- Private/protected attributes ko **read access** provide karta hai  
- Getter method ke jaise kaam karta hai  

**Use:**  
- Encapsulation ke saath data access karne ke liye  
- Attributes ko **safe aur controlled** rakhne ke liye  



### 4️⃣ @name.setter 🔄  
- `@property` ke saath use hota hai  
- Private/protected attributes ki value **update** karne ke liye  
- Data validation aur controlled modification ke liye useful  



**Summary:**  
- Decorators = **methods ko enhance ya modify** karne ka tool 🎀  
- Common decorators = `@classmethod` 🏛️, `@staticmethod` 🛠️, `@property` 💠, `@name.setter` 🔄  
- Benefits = **clean, reusable, maintainable aur secure code** ✨
