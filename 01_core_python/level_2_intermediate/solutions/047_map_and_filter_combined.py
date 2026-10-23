"""Exercise 047 — Map and Filter Combined.

Use map() and filter() to square even numbers in [1,2,3,4,5,6,7,8,9,10].
"""


# Your implementation here

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filterEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


def squareMapper(x):
    return x * x


ansFilter = filter(filterEven, numbers)
ansSqMapper = map(squareMapper, ansFilter)

for x in ansSqMapper:
    print(x)
