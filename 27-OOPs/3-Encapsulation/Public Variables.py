class Person:
    def __init__(self, name):
        self.name = name   # Public

p = Person("CodeQueen")
print(p.name)  # Direct access allowed
