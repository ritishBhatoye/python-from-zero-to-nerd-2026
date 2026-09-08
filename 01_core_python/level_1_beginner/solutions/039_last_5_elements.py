"""Exercise 039 — Last 5 Elements.

Generate list of squares (1-20) and print last 5 elements.
"""

# Your implementation here
pass


ans = []

for i in range(1, 21):
    ans.append(i * i)

print(ans)
for i in range(len(ans) - 5, len(ans)):
    print(ans[i])
