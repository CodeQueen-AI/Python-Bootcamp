Bilkul Code Queen 👑✨, yahan tumhare liye **Python Exceptions & Exception Handling** ka **README file content** hai — headings English, explanation Roman Urdu mein, **code ke bagair**:

---

# ⚠️ Python Exceptions & Exception Handling

## 📘 What is an Exception?

**Exception** ka matlab hai **error jo program run hone ke dauran hoti hai**.
Yani jab Python ko koi **unexpected problem** milti hai, to wo **exception raise** karta hai aur program crash kar sakta hai agar handle na kiya jaye.

---

## 🔹 Common Types of Exceptions

1. **ZeroDivisionError** → Jab number ko zero se divide karte hain.
2. **TypeError** → Jab wrong type ke data ke saath operation karte hain.
3. **ValueError** → Jab value invalid ho kisi function ke liye.
4. **IndexError** → Jab list ya string mein invalid index access karte hain.
5. **KeyError** → Jab dictionary mein non-existing key access karte hain.
6. **FileNotFoundError** → Jab file exist nahi karti aur access karne ki koshish hoti hai.

---

## 🔹 Exception Handling

Python mein **exceptions ko handle karne ke liye `try`, `except`, `else`, aur `finally` use hota hai**.

1. **Try / Except**

   * Risky code ko `try` block mein daalte hain aur agar error aaye to `except` handle karta hai.

2. **Multiple Except**

   * Alag-alag errors ke liye alag messages show kar sakte hain.

3. **Else**

   * Jab koi error na aaye, `else` block execute hota hai.

4. **Finally**

   * Ye hamesha execute hota hai, chahe error aaye ya na aaye.

5. **Raise Exception**

   * Khud se error create kar ke program ka control handle karte hain.

---

## 💡 Why Exception Handling is Important

* Program ko **crash hone se bachata hai**.
* Users ko **friendly error messages** dikhata hai.
* Complex programs mein **robust aur reliable** code likhne mein help karta hai.

---

## ✨ In Short

**Exceptions = Run-time errors**
**Exception Handling = Errors ko safely handle karna taake program smoothly chal sake**

