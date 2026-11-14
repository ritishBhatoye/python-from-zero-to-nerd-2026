"""Exercise 095 — Person Gender Classes.

Define Person with Male and Female subclasses.
"""


# Your implementation here


class Person:
    name = " "
    age = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Male(Person):
    gender = ""

    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = "Male"


class Female(Person):
    gender = ""

    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = "Female"


m = Male("Ritish Bhatoye", 23)
f = Female("Ritika", 22)

print("Male : ", m.name, "Age : ", m.age)
