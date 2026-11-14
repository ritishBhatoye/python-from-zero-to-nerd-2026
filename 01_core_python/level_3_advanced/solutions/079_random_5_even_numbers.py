"""Exercise 079 — Random 5 Even Numbers.

Generate list with 5 random even numbers 100-200.
"""

# Your implementation here
import random

ans = []

for i in range(5):
    if i % 2 == 0:
        ans.append(random.randint(100, 200))

print(ans)
