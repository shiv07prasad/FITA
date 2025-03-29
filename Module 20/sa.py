class Father:

    def __init__(self,side):
        self.side = side

    def work(self):
        return "Engineer"

class Mother:
    def __init__(self, vec):
        self.vec = vec

    def hobby(self):
        return "Painting"

class Child(Father, Mother):  # Inherits from both Father & Mother
    def __init__(self,side,vec):
        super().__init__(side)
        super().__init__(self,vec)

c = Child(5,7)
print(c.vec)
print(c.side)
print(c.work())   # Output: Engineer
print(c.hobby())  # Output: Painting