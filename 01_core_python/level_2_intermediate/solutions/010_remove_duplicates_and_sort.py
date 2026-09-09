"""Exercise 010 — Remove Duplicates and Sort.

Remove duplicate words and sort alphanumerically.
"""

# Your implementation here
pass


lines = input("Enter the line : ")

words = sorted(set(lines.split()))

result = ("").join(words)

print(words)
