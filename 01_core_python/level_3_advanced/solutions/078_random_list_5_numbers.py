"""Exercise 078 — Random List 5 Numbers.

Generate list with 5 random numbers between 100-200.
"""

import random

ans = []
for i in range(100, 200):
    if len(ans) == 5:
        break
    ans.append(random.randint(i))

print(ans)
