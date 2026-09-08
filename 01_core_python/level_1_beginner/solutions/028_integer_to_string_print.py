"""Exercise 028 — Integer to String Print.

Define a function that converts an integer into a string and prints it.
"""

# Your implementation here
pass


def toString(a):
    print("Number ", a)
    return str(a)


a = int(input("Enter a number : "))
print("Type of ", a, " before conversion to string ", type(a))

a = toString(a)

print("Type of ", a, " after conversion to string ", type(a))
