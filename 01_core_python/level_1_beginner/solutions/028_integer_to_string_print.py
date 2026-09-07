"""Exercise 028 — Integer to String Print.

Define a function that converts an integer into a string and prints it.
"""

# Your implementation here
pass


def toString(a):
    str(a)
    print("Number ", a)


a = int(input("Enter a number : "))
print("Type of ", a, " before conversion to string ", type(a))

a = toString(a)

print("Type of ", a, " after conversion to string ", type(a))
