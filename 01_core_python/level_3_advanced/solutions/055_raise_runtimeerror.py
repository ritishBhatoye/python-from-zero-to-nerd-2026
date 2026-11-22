"""Exercise 055 — Raise RuntimeError.

Raise a RuntimeError exception.
"""


# Your implementation here
def raiseRT():
    try:
        result = 5 / 0
        print(result)
    except:
        print("Error : Denominator cannot be 0")


raiseRT()
