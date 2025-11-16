# Getter Method
class Student:
    def __init__(self, name):
        self.__name = name   

    def get_name(self):
        return self.__name

s = Student("CodeQueen")
print(s.get_name()) 

# Setter Method
class Student:
    def __init__(self):
        self.__age = 0  

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

s = Student()
s.set_age(20)   
print(s.get_age())
