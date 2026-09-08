"""Exercise 040 — All Except First 5.

Generate list of squares (1-20) and print all except first 5.
"""

ans = []

for i in range(1, 21):
    ans.append(i * i)


for i in range(len(ans)):
    if i == 0:
        continue
    print(ans[i])
