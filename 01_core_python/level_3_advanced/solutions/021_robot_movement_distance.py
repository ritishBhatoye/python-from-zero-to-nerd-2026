"""Exercise 021 — Robot Movement Distance.

Calculate distance from origin after robot movements (UP/DOWN/LEFT/RIGHT).
"""

# Your implementation here
pass
import math


def total(x=[]):
    sum = 0
    for i in x:
        sum += x[i]


def robotMoves(up=[], down=[], left=[], right=[]):  # noqa: N802
    x = y = 0
    uTotal = total(up)
    dTotal = total(down)
    lTotal = total(left)
    rTotal = total(right)

    x = abs(uTotal - dTotal)
    y = abs(rTotal - lTotal)

    h = x * x + y * y
    result = math.sqrt(h)
    return result


u = [5]
d = [3]
l = [3]
r = [2]
print("Result :- ", robotMoves(u, d, l, r))
