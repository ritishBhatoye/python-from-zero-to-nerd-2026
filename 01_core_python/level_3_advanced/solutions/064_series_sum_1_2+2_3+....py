"""Exercise 064 — Series Sum 1/2+2/3+....

Compute 1/2+2/3+3/4+...+n/(n+1) for given n.
"""

# Your implementation here
pass

n = int(input("Enter the value for n : "))


def cal(n):
    sum = 0
    for i in range(1, n):
        sum += i / i + 1


print("Sum : ", cal(n))
