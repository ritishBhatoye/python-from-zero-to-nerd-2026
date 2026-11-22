"""Exercise 050 — Static Method Class.

Define class with static method printNationality.
"""

# Your implementation here


class STMethod:
    @staticmethod
    def print_nationality(nationality):
        return nationality


print(STMethod.print_nationality("American"))
