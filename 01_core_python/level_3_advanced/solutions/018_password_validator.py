"""Exercise 018 — Password Validator.

Validate passwords based on criteria: [a-z], [A-Z], [0-9], [$#@], length 6-12.
"""

# Your implementation here
pass


password = input("Enter the password : ")


def passwordValidator(x):
    if (
        any(c.islower() for c in x)
        and any(c.isupper() for c in x)
        and any(c.isdigit() for c in x)
        and any(c in "@#$" for c in x)
        and len(x) >= 6
        and len(x) <= 12
    ):
        print("Password is created ")
    else:
        print("Please re-enter the password")


passwordValidator(password)
