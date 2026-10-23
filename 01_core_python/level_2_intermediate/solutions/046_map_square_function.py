"""Exercise 046 — Map Square Function.

Use map() to square elements in [1,2,3,4,5,6,7,8,9,10].
"""

# Your implementation here
pass

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sqMapper(x):
    return x * x


ans = map(sqMapper, elements)

for x in ans:
    print(x)
