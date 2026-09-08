"""Exercise 040 — All Except First 5.

Generate list of squares (1-20) and print all except first 5.
"""

# Your implementation here
pass


ans = []

for i in range(1, 21):
    ans = i * i


for i in ans:
    print(ans[i])
