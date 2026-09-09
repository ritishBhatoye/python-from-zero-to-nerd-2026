"""Exercise 008 — Sort Words Alphabetically.

Sort comma-separated words alphabetically.
"""

# Your implementation here
pass

words = input("Enter the test cases ")

words = words.split(",")

words.sort()

result = ",".join(words)

print(result)
