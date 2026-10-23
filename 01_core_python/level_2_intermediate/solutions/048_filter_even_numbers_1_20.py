"""Exercise 048 — Filter Even Numbers 1-20.

Use filter() to get even numbers between 1-20.
"""

# Your implementation here
pass

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def filterEvenNums(x):
    if x % 2 == 0:
        return True
    else:
        return False


ans = filter(filterEvenNums, numbers)

for x in ans:
    print(x)
