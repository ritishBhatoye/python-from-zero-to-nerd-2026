"""Exercise 003 — Dictionary of Squares.

Generate a dictionary that contains (i, i*i) for i from 1 to n (both included).
"""

# Your implementation here
squares = {}

n = int(input("Enter the number :- "))

for index, num in enumerate(range(1, n + 1)):
    squares[index] = index * index


print(squares)
