student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

# get(key) 
print("Name:", student.get("name"))
print("Grade:", student.get("grade", "Not Available")) 

# update() 
student.update({"age": 21, "grade": "A"})
print("Updated Dictionary:", student)

# pop(key)
age = student.pop("age")
print("Removed Age:", age)
print("After pop:", student)

# popitem() 
last_item = student.popitem()
print("Removed Last Item:", last_item)
print("After popitem:", student)

# clear() 
student.clear()
print("After clear:", student)
