# 📦 Import & Export in Python

**Definition:**
Python me **import/export ka matlab hai ek file ya module ka code dusri file me use karna**.

**Use:**

* Ek file ke functions, classes, variables ko **dusri file me access** karne ke liye
* Code ko **modular aur reusable** banane ke liye

**Why We Use Import & Export:**

* Code repetition avoid karne ke liye
* Large projects me **organized aur clean structure** maintain karne ke liye
* Ek hi function ko multiple files me **reuse** karne ke liye



## 🔹 Key Points About Import & Export

1. **Importing Modules:**

   * Dusri file ya built-in module ka code apni file me **access** karne ke liye `import` use hota hai

2. **Exporting Functions / Variables:**

   * Ek file me define kiye functions, variables ya classes **dusri file me use karne ke liye export** kiye ja sakte hain (by default Python me public hote hain).

3. **Accessing Imported Code:**

   * Imported module ke content ko **module_name.function_name** ke through call karte hain.

4. **`__pycache__` Folder:**

   * Jab Python koi file run karta hai, to **compiled bytecode (.pyc files)** ko **`__pycache__` folder** me store karta hai.
   * **Purpose:**

     * Agle runs me Python ko **faster execution** ke liye code dobara compile nahi karna padta
     * Execution speed improve hoti hai
   * Ye folder **automatically generate hota hai** aur aapke source code ko affect nahi karta.



✨ **Summary:**

* Import & Export = **Code reuse aur modular programming** ✅
* Python me `import` se **functions, classes aur variables** ko easily reuse kar sakte ho
* Large projects ke liye **essential concept** hai
* **`__pycache__`** = Python ka **bytecode cache system** ⚡, faster execution ke liye


