person = {
    'name': 'CodeQueen',
    'age': 18,
    'city': 'Karachi'
}
print(person)

# keys() → returns all keys
print(person.keys())

# values() → returns all values
print(person.values())

# items() → returns all key-value pairs as tuples
print(person.items())

# get(key) → returns value for the key (None if key doesn't exist)
print(person.get("name"))   
print(person.get("grade"))

# update() → adds or updates key-value pairs
person.update({"age": 21, "grade": "A"})
print(person)

# pop(key) → removes a key and returns its value
age = person.pop("age")
print(age)

# popitem() → removes and returns the last inserted key-value pair
last_item = person.popitem()
print(last_item)

# clear() → removes all items
person.clear()
print(person)
