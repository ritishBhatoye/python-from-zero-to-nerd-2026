"""Exercise 089 — Remove Even Indexed Elements.

Remove 0th,2nd,4th,6th elements using enumerate.
"""

# Your implementation here
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


result = [num for index, num in enumerate(numbers) if index % 2 != 0]

print(result)
