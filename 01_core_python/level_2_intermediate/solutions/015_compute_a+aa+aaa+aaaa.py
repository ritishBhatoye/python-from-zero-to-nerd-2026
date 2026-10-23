"""Exercise 015 — Compute a+aa+aaa+aaaa.

Compute a+aa+aaa+aaaa with given digit a.
"""

# Your implementation here
pass

a = input("Enter the digit : ")

n1 = a
n2 = 2 * a
n3 = 3 * a
n4 = 4 * a

sum = int(n1) + int(n2) + int(n3) + int(n4)

print(sum)
