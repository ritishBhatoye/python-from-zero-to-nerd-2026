"""Exercise 043 — Filter Even Numbers Tuple.

Generate tuple with even numbers from (1,2,3,4,5,6,7,8,9,10).
"""

# Your implementation here
pass

ans = ()

for x in range(1, 11):
    if x % 2 == 0:
        ans.append(x)

print(ans)
