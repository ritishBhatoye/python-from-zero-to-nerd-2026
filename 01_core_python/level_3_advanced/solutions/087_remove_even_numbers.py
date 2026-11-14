"""Exercise 087 — Remove Even Numbers.

Remove even numbers from list using comprehension.
"""

# Your implementation here
pass


even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = [num for num in even if num % 2 != 0]
print(odd)
