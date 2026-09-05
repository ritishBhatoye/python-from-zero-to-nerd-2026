"""Exercise 002 — Factorial Calculator.

Compute the factorial of a given number. Input: 8, Output: 40320
"""

# Your implementation here
pass


n = int(input("Enter the number :- "))


def fac(x):
    if x == 1:
        return 1

    x * fac(x - 1)
