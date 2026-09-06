"""Exercise 004 — Comma Separated to List and Tuple.

Accept comma-separated numbers and generate a list and a tuple.
"""

# Your implementation here
pass

numbers = input("Enter the numbers :- ")

ansList = []
ansTuple = ()

for n in numbers:
    if n == "," or n.isalpha():
        continue
    else:
        ansList.append(n)


ansTuple = tuple(ansList)

print(ansList)
print(ansTuple)
