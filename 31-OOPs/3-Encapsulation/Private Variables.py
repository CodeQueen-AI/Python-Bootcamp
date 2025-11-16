class Person:
    def __init__(self, name):
        self.__name = name   # Private

p = Person("CodeQueen")
# print(p.__name)  # ❌ Error
