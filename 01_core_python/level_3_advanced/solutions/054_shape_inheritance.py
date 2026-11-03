"""Exercise 054 — Shape Inheritance.

Define Shape class and Square subclass with area methods.
"""

# Your implementation here
pass


class Shape:
    def __init__(self):
        print("hey from shape class")


class Square(Shape):
    side = 0

    def __init__(self, side):
        self.side = side

    def area(self):
        s = self.side
        return s * s


s = Square(9)

print("Area : ", s.area())
