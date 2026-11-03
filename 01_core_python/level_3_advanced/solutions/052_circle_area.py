"""Exercise 052 — Circle Area.

Define Circle class that can compute area.
"""

# Your implementation here
pass


class Circle:
    r = 1.0

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * float(self.r) * float(self.r)


c = Circle("5")
print("Area : ", c.area())
