"""Exercise 053 — Rectangle Area.

Define Rectangle class that can compute area.
"""

# Your implementation here
pass


class Rectangle:
    height = 0
    width = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        l = self.height
        b = self.width

        return l * b


r = Rectangle(4, 5)
print("Area : ", r.area())
