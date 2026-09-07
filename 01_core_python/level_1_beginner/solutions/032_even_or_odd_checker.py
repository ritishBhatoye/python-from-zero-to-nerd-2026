"""Exercise 032 — Even or Odd Checker.

Print 'It is an even number' or 'It is an odd number' based on input.
"""

# Your implementation here
pass


def isEvenOrOdd(n):
    if n % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")


n = int(input("Enter the number :- "))
isEvenOrOdd(n)
