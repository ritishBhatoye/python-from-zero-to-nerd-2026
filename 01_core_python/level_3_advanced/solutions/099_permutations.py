"""Exercise 099 — Permutations.

Print all permutations of [1,2,3].
"""

# Your implementation here
from itertools import permutations

l = [1, 2, 3]

for i in permutations(l):
    print(list(i))
