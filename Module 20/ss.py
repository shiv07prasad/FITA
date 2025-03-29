class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

class Car(Vehicle):
    def __init__(self,max_speed, brand):
        super().__init__(max_speed)
        self.brand = brand

my_car = Car(200, "Toyota")
print(my_car.brand, my_car.max_speed)  # Output: Toyota 200


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Calls Animal's __init__ with name & age
        self.breed = breed

dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.name, dog.age, dog.breed)  # Output: Buddy 3 Golden Retriever
