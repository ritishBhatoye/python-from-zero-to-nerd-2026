"""Exercise 051 — Class Inheritance.

Define American class and NewYorker subclass.
"""


# Your implementation here


class American:
    name = ""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class NewYorker(American):
    pass


subclass = NewYorker("Ritish Bhatoye")
print(subclass.get_name())
