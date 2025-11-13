# 📅 Python Date Manipulation

## 📘 What is Date Manipulation?

**Date Manipulation** ka matlab hota hai Python mein **dates aur times ke saath kaam karna**, jaise ke current date lena, format change karna, difference nikalna, aur future/past dates calculate karna.
Ye sab kaam **datetime module** ke zariye kiye jaate hain.



## 🔹 Important Concepts

1. **Current Date & Time**

   * `datetime.now()` se current date aur time milta hai.

2. **Today's Date**

   * `date.today()` sirf aaj ki date return karta hai.

3. **Specific Date Create Karna**

   * `datetime.date(year, month, day)` se manually koi bhi date banayi ja sakti hai.

4. **Formatting Date**

   * `strftime()` method se date ko readable format mein convert karte hain, jaise `"2025-11-13"` → `"13-11-2025"`.

5. **String to Date Convert Karna**

   * `strptime()` ka use karke string ko date object mein badalte hain.

6. **Date Difference Nikalna**

   * `timedelta` ka use karke do dates ke beech ka difference (days) nikalte hain.

7. **Add/Subtract Days**

   * `timedelta(days=10)` se future ya past dates calculate karte hain.

---
## 🧠 Common Functions

| Function                  | Description                                         |
| ------------------------- | --------------------------------------------------- |
| `datetime.datetime.now()` | Current date aur time deta hai                      |
| `datetime.date.today()`   | Sirf current date deta hai                          |
| `strftime()`              | Date ko custom format mein convert karta hai        |
| `strptime()`              | String ko date object mein badalta hai              |
| `timedelta()`             | Date difference aur arithmetic ke liye use hota hai |



## 💡 Why Use Date Manipulation

* Reports aur logs banane ke liye
* Expiry ya due dates calculate karne ke liye
* Scheduling aur reminders ke liye
* Data analysis mein time period compare karne ke liye



## ✨ In Short

**Date Manipulation** ka matlab hai **dates aur times ke sath smart tarike se kaam karna** — unhe format karna, compare karna, aur modify karna.

