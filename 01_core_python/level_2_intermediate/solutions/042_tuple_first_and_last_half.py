"""Exercise 042 — Tuple First and Last Half.

With tuple (1,2,3,4,5,6,7,8,9,10), print first half and last half separately.
"""

# Your implementation here
pass

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

end = int(len(t))
mid = int(end / 2)

print(t[:mid])
print(t[mid:])
