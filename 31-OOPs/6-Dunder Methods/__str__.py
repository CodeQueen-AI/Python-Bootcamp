class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}"

s = Student("CodeQueen", 20)
print(s)   # __str__ automatically call hota hai
