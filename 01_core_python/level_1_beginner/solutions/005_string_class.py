"""Exercise 005 — String Class.

Define a class with getString and printString methods. printString prints in uppercase.
"""

# Your implementation here
pass


class String:
    def getString(self):
        self.s = input("Enter the string")

    def printString(self):
        print(self.s.upper())


s = String()

s.getString()
s.printString()
