# 🐍 Python Scope

## 📘 What is Scope?

Scope ka matlab hai program ke andar wo area jahan koi variable use ya access kiya ja sakta hai.
Simple lafzon mein, scope batata hai ke variable **kahan visible hai aur kahan nahi**.



## 💡 Why We Use Scope

Scope use karne ka maqsad ye hota hai:

* Variables ko sahi tarike se organize karna.
* Program mein same name ke variables ke conflicts se bachna.
* Data ko safe rakhna aur sirf us jaga use karna jahan zarurat ho.


## 🔹 Types of Scope in Python

Python mein mainly **do types ke scope** hotay hain 👇

### 1. **Local Scope**

* Ye wo variables hotay hain jo **function ke andar declare** kiye jaate hain.
* Ye sirf **usi function ke andar** use ho sakte hain.
* Function ke bahar inko access nahi kiya ja sakta.

### 2. **Global Scope**

* Ye wo variables hotay hain jo **function ke bahar declare** kiye jaate hain.
* Ye **poore program mein** kahin bhi use kiye ja sakte hain, hatta ke functions ke andar bhi.



## 🧠 Summary

| Type   | Declared Where    | Accessible Where       | Example                |
| ------ | ----------------- | ---------------------- | ---------------------- |
| Local  | Function ke andar | Sirf function ke andar | `x` in `def my_func()` |
| Global | Function ke bahar | Har jaga               | `y` declared outside   |



## ✨ In Short

Scope ka matlab hai **variable ka visible area**.
Ye ensure karta hai ke variables ko sahi aur logical jagah par use kiya jaye.
