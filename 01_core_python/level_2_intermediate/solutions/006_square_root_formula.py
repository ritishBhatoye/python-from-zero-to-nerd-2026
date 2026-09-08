"""Exercise 006 — Square Root Formula.

Calculate Q = sqrt((2*C*D)/H) where C=50, H=30, D is comma-separated input.
"""

# Your implementation here
import math

C = 50
H = 30

D = input().split(",")

ans = []

for d in D:
    d = int(d)
    Q = math.sqrt((2 * C * d) / H)
    ans.append(Q)

print(ans)
