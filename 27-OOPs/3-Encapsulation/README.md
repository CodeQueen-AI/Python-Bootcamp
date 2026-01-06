# Encapsulation in Python 🔒

**Encapsulation kya hai?**  
Encapsulation OOP ka ek concept hai jisme hum **data aur methods ko class ke andar protect** karte hain.  
Ye ensure karta hai ke **data safe aur secure** rahe aur program organized ho. ✨

**Encapsulation kyun use karte hain?**  
- Data ko **direct access se protect** karne ke liye  
- Class ke **internal implementation ko hide** karne ke liye  
- Program ko **secure aur maintainable** banane ke liye  
- Objects ke **data integrity** ko maintain karne ke liye  

---

## 🔹 Types of Variables in Encapsulation

### 1️⃣ Public Variables 🌐  
- Sab objects ke liye **accessible** hote hain  
- Directly read aur modify kiye ja sakte hain  

### 2️⃣ Protected Variables 🟡  
- Single underscore `_var` se indicate hota hai  
- Conventionally child classes ke liye accessible hota hai, **direct access avoid** karna chahiye  

### 3️⃣ Private Variables 🔒  
- Double underscore `__var` se indicate hota hai  
- Sirf **class ke andar access possible**  
- Bahar se access karna avoid karna chahiye  

---

## 🔹 Getter & Setter Methods 🛠️  

**Getter Methods**  
- Private/protected variables ki value **read karne ke liye** use hote hain  

**Setter Methods**  
- Private/protected variables ki value **update karne ke liye** use hote hain  
- Data validation ke liye useful hote hain  

**Benefits:**  
- Data **secure aur controlled** rehta hai  
- Class ke **internal structure ko hide** karte hain  
- Program ka behavior **predictable aur safe** banta hai  


**Summary:**  
- Encapsulation = **data aur methods ko protect karna** 🔒  
- Variables = Public 🌐, Protected 🟡, Private 🔒  
- Getter & Setter = **controlled access aur modification** 🛠️  
- Benefits = **security, maintainability, data integrity**
