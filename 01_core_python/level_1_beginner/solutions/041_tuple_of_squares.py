"""Exercise 041 — Tuple of Squares.

Generate and print a tuple of squares from 1-20.
"""

ans = ()

for i in range(1, 21):
    ans = ans + (i * i,)

print(ans)
