# Run-time / Method Overriding
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

p = Parent()
c = Child()

p.greet()   # Parent ka method
c.greet()   # Child ka method
