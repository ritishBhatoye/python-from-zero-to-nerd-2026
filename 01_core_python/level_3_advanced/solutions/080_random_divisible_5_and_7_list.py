"""Exercise 080 — Random Divisible 5 and 7 List.

Generate 5 numbers divisible by 5 and 7 from 1-1000.
"""

# Your implementation here

import random

ans = []

for i in range(5):
    if i % 5 == 0 and i % 7 == 0:
        ans.append(random.randint(1, 1000))

print(ans)
