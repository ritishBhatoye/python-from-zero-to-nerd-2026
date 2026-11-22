"""Exercise 069 — Generator Divisible 5 and 7.

Use generator for numbers divisible by both 5 and 7.
"""

# Your implementation here
pass


ans = []


def genFS(x):
    for i in range(1, x):
        if i % 5 == 0 and i % 7 == 0:
            yield i
        else:
            continue


for num in genFS(101):
    print(num)
