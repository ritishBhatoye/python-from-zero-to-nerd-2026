"""Exercise 021 — Robot Movement Distance.

Calculate distance from origin after robot movements (UP/DOWN/LEFT/RIGHT).
"""

# Your implementation here
pass


def total(x=[]):
    sum = 0
    for i in x:
        sum += x[i]


def func(up=[], down=[], left=[], right=[]):
    x = y = 0
    uTotal = total(up)
    dTotal = total(down)
    lTotal = total(left)
    rTotal = total(right)

    if uTotal > dTotal:
        x = uTotal - dTotal
    elif dTotal > uTotal:
        x = dTotal - uTotal

    if lTotal < rTotal:
        y = lt
