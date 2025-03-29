from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod  # Abstract class, but not enforcing method implementation
    def start_engine(self,kl):
        return kl# This is now a normal method, not an enforced abstract method

class Car(Vehicle):  # Concrete class
    def start_engine(self):
        return "yyy"

class Bike(Vehicle):  # Another concrete class
    def start_engine(self):
        return "Bike engine started!"

# Now, we can create an instance of Vehicle
# v = Vehicle()
# print(v.start_engine())  # Output: None (because the method exists but does nothing)

c = Car()
print(c.start_engine())  # Output: None (Car inherited the empty method from Vehicle)

b = Bike()
print(b.start_engine())  # Output: "Bike engine started!"
