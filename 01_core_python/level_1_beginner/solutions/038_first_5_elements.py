"""Exercise 038 — First 5 Elements.

Generate list of squares (1-20) and print first 5 elements.
"""

# Your implementation here
pass


ans = {}

for n in range(1, 21):
    ans[n] = n * n


for i in range(1, 6):
    print(ans[i])
