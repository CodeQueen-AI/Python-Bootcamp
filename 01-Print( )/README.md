## 🖨️ What is print() Function?

`print()` function is used to show/output text, numbers, or results on the screen.

Example:

```
print("My name is CodeQueen!")
```

This will display:

```
My name is CodeQueen!
```


## ✅ What are print() Parameters?

print() function ke kuch extra options hote hain jinko **parameters** kehte hain. Ye parameters output ko control karte hain ke screen par text kese dikhaye.
print() function has some optional settings (parameters) that change how output is displayed on the screen.

The most useful parameters are:

* **sep** → controls the separator between values
* **end** → controls what is printed at the end of a line
* **flush** → controls whether output is shown immediately or not



## 🔹 sep Parameter

**sep** ka matlab separator hota hai.
Jab hum multiple cheezen print karte hain to **unke beech kya aana chahiye** usay sep decide karta hai.

💡 Default: Space aata hai words ke beech.
**sep** (separator) is used when printing multiple values together.
It defines which symbol or space will come **between** the printed values.

✅ Default: A single space is used between words.

👉 Use **sep** when you want custom formatting between words/numbers.



## 🔹 end Parameter

**end** decide karta hai ke print hone ke baad **aakhri mei kya aye**.

💡 Default: New line (har print nayi line se start hota hai).

✅ end ka use tab hota hai jab hume same line par output continue karna ho.
**end** is used to change what appears **after** the printed output.

✅ Default: A **new line** starts after every print.

👉 Use **end** to continue printing on the same line or add custom characters at the end.



## 🔹 flush Parameter

**flush** batata hai ke output **turant screen par show ho ya baad mei**.

💡 Default: `flush=False`
→ Pehle output memory mei store hota hai, phir screen par show hota hai.

✅ Agar `flush=True` ho:
→ Output **immediately** show hota hai, bilkul delay nahi hota.

Ye zyada tar **live updates**, **countdown**, **progress bar** jese kaamon mei use hota hai.

| flush Value                                                  | Behavior                              |
| ------------------------------------------------------------ | ------------------------------------- |
| False                                                        | Output late ya delay se show hota hai |
| True                                                         | Output foran show hota hai            |
| **flush** controls how quickly output appears on the screen. |                                       |

✅ Default: `flush=False` → Output is stored temporarily and may appear later.

✅ When we set `flush=True`:

* Output appears **immediately**
* Specially useful in **live updates**, progress bars, countdowns, etc.

So:

| flush Value     | Output Behavior        |
| --------------- | ---------------------- |
| False (default) | Output may delay       |
| True            | Output shows instantly |



📌 These print() parameters help control formatting and behavior of your output, making programs look cleaner and more professional

