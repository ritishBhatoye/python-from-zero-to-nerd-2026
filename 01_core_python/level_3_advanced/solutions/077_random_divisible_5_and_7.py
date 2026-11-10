"""Exercise 077 — Random Divisible 5 and 7.

Output random number divisible by both 5 and 7.
"""

# Your implementation here
import random

ans = []
for i in range(1, 101):
    if i % 7 == 0 and i % 5 == 0:
        ans.append(i)
num = random.choice(ans)
print(num)
