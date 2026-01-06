class Parent:
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")

c = Child()
c.show_parent()
c.show_child()
# Parent Class
class Animal:
    def sound(self):
        print("Animals make sounds")

# Child Class (inherits Animal)
class Dog(Animal):
    pass

# Object of Child Class
d = Dog()
d.sound()     # Parent ka method child ko mil gaya
