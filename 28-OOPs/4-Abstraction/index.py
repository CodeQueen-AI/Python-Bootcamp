from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass  # abstract method, koi implementation nahi

# Derived class
class Dog(Animal):
    
    def sound(self):
        print("Woof Woof 🐶")  # implementation

class Cat(Animal):
    
    def sound(self):
        print("Meow 😺")  # implementation

# Objects
dog = Dog()
dog.sound()  # Output: Woof Woof 🐶

cat = Cat()
cat.sound()  # Output: Meow 😺
