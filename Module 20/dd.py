class Animal:  # Parent class

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):  # Child class
    def speak(self):
        return "Bark!"

d = Dog("Jhony")
print(d.name)
print(d.speak())