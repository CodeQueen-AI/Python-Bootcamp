# Dictionary : Dictionaries in Python are unordered, changeable and key-value pairs based data 
# structures They are defined using curly braces `{}`
person = {"name": "CodeQueen", "age": 17, "city": "Karachi"}
print(person)

# Using dict() Constructor
student = dict(name="Anusha", age=20, grade="A")
print(student)

# Accessing Elements
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}
print("Name:", student["name"])
print("Age:", student["age"])