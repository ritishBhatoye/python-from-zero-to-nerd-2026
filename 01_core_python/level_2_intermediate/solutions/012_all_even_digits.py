"""Exercise 012 — All Even Digits.

Find numbers between 1000-3000 where each digit is even.
"""

# Your implementation here
pass

ans = []
for i in range(1000, 3001):
    if i % 2 == 0:
        ans.append(i)

for i in ans:
    print(i)
