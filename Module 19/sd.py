class Dog:
    species = "Canis familiaris"  # Class attribute
    
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute
        print(name)
    
    def r(self):
        print(self.name)
print(Dog.r)
