# **Python Strings Guide 📖**

Python me **strings** text data ko represent karte hain. Strings **immutable** hote hain, iska matlab ye hai ke unko directly modify nahi kiya ja sakta.

Strings ka use **text storage, manipulation aur display** ke liye hota hai.


## **1️⃣ String Types 📝**

* **Single Quotes `' '`** → Simple text define karne ke liye
* **Double Quotes `" "`** → Single quotes ke andar text ke liye
* **Triple Quotes `''' '''` ya `""" """`** → Multiline text define karne ke liye
* **Empty String `""`** → Koi value na ho

**Use:** Text ko variables me store aur display karne ke liye



## **2️⃣ String Properties 🔢**

* **Length** → `len()` se string ka size pata chal sakta hai
* **Indexing `[ ]`** → Har character ka position `[0, 1, 2…]` se access hota hai

  * Negative indexing `[-1, -2…]` → End se count karke access

**Use:** Kisi specific character ko access karne ke liye



## **3️⃣ String Methods 🛠️**

### **Case Methods 🔤**

* `.upper()` → Sare letters **uppercase** me convert
* `.lower()` → Sare letters **lowercase** me convert
* `.capitalize()` → Sirf **first character** uppercase, baaki lowercase
* `.swapcase()` → Uppercase ↔ Lowercase swap

**Use:** Strings ke **case ko control aur format** karne ke liye



### **Trimming / Cleaning 🧹**

* `.strip()` → String ke start aur end se **extra spaces remove** karta hai

**Use:** User input ya text clean karne ke liye



### **Replacement & Search 🔍**

* `.replace(old, new)` → Old text ko new se replace karta hai
* `.find(substring)` → Substring ki **position** find karta hai
* `.count(substring)` → Substring **kitni baar** aayi, count karta hai

**Use:** Strings me **modify aur search** karne ke liye



### **Splitting & Joining ✂️➕**

* `.split(separator)` → String ko **list me divide** karta hai
* `.join(iterable)` → List ya iterable ko **ek string me combine** karta hai

**Use:** Text ko **divide aur combine** karne ke liye



### **Check Methods ✅**

* `.isalpha()` → Sirf letters hain
* `.isdigit()` → Sirf numbers hain
* `.isalnum()` → Letters + numbers (special characters nahi)

**Use:** Strings ki **validity check** karne ke liye



## **4️⃣ String Slicing ✂️**

* **Basic Slicing `[start:end]`** → Start se end-1 tak characters extract
* **From start `[:end]`** → Beginning se end tak
* **From position `[start:]`** → Start se string ke end tak
* **Negative Indexing `[-x:]`** → End se characters extract
* **Step `[start:end:step]`** → Characters skip karke extract
* **Reverse `[:: -1]`** → String ko ulta karna

**Use:** Strings ke **sub-parts extract aur manipulate** karne ke liye



## **5️⃣ Summary ✨**

* Strings **immutable** hote hain → Direct modify nahi kar sakte
* **Indexing aur slicing** → Characters access aur sub-parts extract
* **Methods** → Strings ko manipulate, clean, search aur validate karna
* **Split & Join** → Strings ko divide aur combine karna
* **Check methods** → Validity aur content check

**Strings methods aur slicing se aap text ko efficiently manipulate aur control kar sakte ho** 💡

