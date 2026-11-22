"""Exercise 078 — Random List 5 Numbers.

Generate list with 5 random numbers between 100-200.
"""

import random

ans = []
for i in range(5):
    ans.append(random.randint(100, 200))

print(ans)
