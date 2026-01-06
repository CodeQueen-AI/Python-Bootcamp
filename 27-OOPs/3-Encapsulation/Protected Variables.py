class Person:
    def __init__(self, name):
        self._name = name  # Protected

p = Person("CodeQueen")
print(p._name)   # Access possible but conventionally avoid
