"""Exercise 068 — Generator Even Numbers.

Use generator to print even numbers between 0 and n.
"""

# Your implementation here
pass


def genEven():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i


for num in genEven():
    print("Generating even numbers :- ", num)
