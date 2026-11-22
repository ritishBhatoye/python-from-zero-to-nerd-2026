"""Exercise 098 — Even Index Characters.

Print characters at even indices.
"""


# Your implementation here

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(l)):
    if i % 2 == 0:
        print(l[i])
