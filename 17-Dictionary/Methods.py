person = {
    'name' : 'CodeQueen',
    'age' : 18,
    'city' : 'Karachi'
}
print(person)

# keys()
print(person.keys())

# values()
print(person.values())

# items()
print(person.items())

# get(key) 
print(person.get("name"))
print(person.get("grade")) 

# update() 
person.update({"age": 21, "grade": "A"})
print(person)

# pop(key)
age = person.pop("age")
print(age)

# popitem() 
last_item = person.popitem()
print(last_item)

# clear() 
person.clear()
print(person)
