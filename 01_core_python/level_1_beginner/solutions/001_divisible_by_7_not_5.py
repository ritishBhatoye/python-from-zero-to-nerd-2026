"""Exercise 001 — Divisible by 7 not 5.

Find all numbers divisible by 7 but not a multiple of 5, between 2000 and 3200 (both included).
"""

# Your implementation here
pass

ans = []

for n in range(2000, 3201):
    if n % 7 == 0:
        ans.append([n])


for num in ans:
    print(num)
