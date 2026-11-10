"""Exercise 070 — Assert Even Numbers.

Use assert to verify all numbers in [2,4,6,8] are even.
"""

# Your implementation here
pass


numbers = [2, 4, 6, 1, 8]

for num in numbers:
    assert num % 2 == 0

print("All numbers are even!")
