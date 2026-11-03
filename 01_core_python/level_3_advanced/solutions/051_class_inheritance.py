"""Exercise 051 — Class Inheritance.

Define American class and NewYorker subclass.
"""


# Your implementation here


class American:
    name = " "

    def __init__(self, name):
        name = self.name
        print("Hanji mitro")


class NewYorker(American):
    def get_name(self):
        return self.name
