from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  # method ka implementation derived class me hoga

# Derived Class
class Square(Shape):
    
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

# Object
sq = Square(4)
print(sq.area())  # Output: 16
