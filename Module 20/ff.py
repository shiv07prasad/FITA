class Father:
    def __init__(self, side):
        self.side = side

    def work(self):
        return self.side * self.side

class Mother(Father):
    def __init__(self, radius):
        self.radius = radius

    def hobby(self):
        return 3.14 * self.radius ** 2

class Child(Mother):  # Multiple inheritance
    def __init__(self, side, radius):
        Father.__init__(self, side)  # Initialize Father
        Mother.__init__(self, radius)  # Initialize Mother

c = Child(2, 3)  # Now both parents are initialized
print(c.work())   # Output: 4
print(c.hobby())  # Output: 28.26

