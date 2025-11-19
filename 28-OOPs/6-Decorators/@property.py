class Student:
    def __init__(self, name):
        self.__name = name   # Private variable

    # Getter
    @property
    def name(self):
        return self.__name

    # Setter
    @name.setter
    def name(self, value):
        self.__name = value

# Object
s = Student("CodeQueen")
print(s.name)    # Access like normal variable

s.name = "Anusha"  # Update using setter
print(s.name)
