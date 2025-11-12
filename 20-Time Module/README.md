# **📂 Python Time Module – README**

**Time Module** Python ka built-in module hai jo program me **time-related operations** perform karne ke liye use hota hai.
Isse hum program ko pause kar sakte hain, current time access kar sakte hain, aur time ko different formats me display kar sakte hain.


## **💡 Why We Use Time Module**

* Program me **delay** ya **pause** dene ke liye
* **Current time** aur **date** ko access karne ke liye
* Time ko **human-readable format** me display karne ke liye
* Performance measurement ya timed tasks ke liye


## **🛠 How We Use Time Module**

1. **Import the module:**
   Time module ka use karne ke liye sabse pehle `import time` karna padta hai.



## **1️⃣ Pause/Delay (`sleep`)**

* **Definition:** Program ko specified seconds ke liye **rokna**.
* **Purpose:** Countdown, animation, ya tasks ke beech delay create karna.



## **2️⃣ Epoch Time (`time`)**

* **Definition:** Current time ko **seconds since epoch (1 Jan 1970)** me return karta hai.
* **Purpose:** Program execution analysis, timestamp create karna.



## **3️⃣ Human-Readable Time (`ctime`)**

* **Definition:** Current time ko **readable format** me convert karta hai.
* **Purpose:** User-friendly display of current time, jaise `"Tue Nov 5 14:25:10 2025"`.



## **4️⃣ Local Time (`localtime`)**

* **Definition:** Current time ko **tuple** me deta hai (year, month, day, hour, minute, second).
* **Purpose:** Time ke individual components ko access karne ke liye.



## **5️⃣ Custom Format (`strftime`)**

* **Definition:** Time ko **desired/custom format** me display karna.
* **Purpose:** Date/time ko user-friendly ya program-specific format me show karna.



## **6️⃣ Loop + Delay Concept**

* **Definition:** Loops ke saath delay create karna, taki output step-by-step ya timed manner me dikhe.
* **Purpose:** Countdown, animation effects, ya sequential tasks show karne ke liye.



## **✅ Summary Table**

| Feature      | Definition                          | Purpose                          |
| ------------ | ----------------------------------- | -------------------------------- |
| `sleep`      | Program ko pause karta hai          | Delay, countdown, animation      |
| `time`       | Current time in seconds since epoch | Time measurement, timestamp      |
| `ctime`      | Current time human-readable         | User-friendly display            |
| `localtime`  | Time as tuple (year, month, day...) | Access individual components     |
| `strftime`   | Custom formatted time               | Desired date/time format         |
| Loop + Delay | Delay in loops                      | Step-by-step output, timed tasks |

