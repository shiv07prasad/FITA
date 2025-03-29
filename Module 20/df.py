class Father:
    def work(self):
        return "Engineer"

class Mother:
    def hobby(self):
        return "Painting"

class Child(Father, Mother):  # Inherits from both Father & Mother
    pass

c = Child()
print(c.work())   # Output: Engineer
print(c.hobby()) 