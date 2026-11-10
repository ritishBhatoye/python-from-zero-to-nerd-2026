"""Exercise 068 — Generator Even Numbers.

Use generator to print even numbers between 0 and n.
"""

# Your implementation here
pass


def genEven():
    for i in range(0, 10):
        if i % 2 == 0:
            yield i


print("Generating even numbers :- ", genEven())
