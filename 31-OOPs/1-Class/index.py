class Student:

    # Constructor (__init__)  
    def __init__(self, name, age):
        # Attributes (variables)
        self.name = name
        self.age = age

    # Methods
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Object banana 
s1 = Student("CodeQueen", 20)

# Method call
s1.show_info()
