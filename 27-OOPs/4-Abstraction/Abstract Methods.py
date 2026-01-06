from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass  # sirf declare kiya, implementation derived class me

# Derived Class
class Car(Vehicle):
    
    def start_engine(self):
        print("Car engine started 🚗")

class Bike(Vehicle):
    
    def start_engine(self):
        print("Bike engine started 🏍️")

# Objects
car = Car()
car.start_engine()  # Output: Car engine started 🚗

bike = Bike()
bike.start_engine()  # Output: Bike engine started 🏍️
