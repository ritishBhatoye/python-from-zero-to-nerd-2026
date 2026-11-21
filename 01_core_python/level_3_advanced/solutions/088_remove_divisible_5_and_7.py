"""Exercise 088 — Remove Divisible 5 and 7.

Remove numbers divisible by 5 and 7 using comprehension.
"""

# Your implementation here
numbers = [10, 14, 15, 20, 21, 25, 28, 30, 35, 40, 42, 50]

result = [num for num in numbers if num % 5 != 0 and num % 7 != 0]
print(result)
