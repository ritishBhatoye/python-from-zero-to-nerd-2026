"""Exercise 049 — Map Squares 1-20.

Use map() to square numbers between 1-20.
"""

# Your implementation here
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def mapSq(x):
    return x * x


ans = map(mapSq, numbers)

for x in ans:
    print(x)
