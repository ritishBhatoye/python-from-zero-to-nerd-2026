"""Exercise 016 — Filter Odd Numbers.

Use list comprehension to filter odd numbers from comma-separated input.
"""

# Your implementation here
pass

odd = input("Enter comma separated numeric values : ")

newOddList = []

for i in odd:
    if i % 2 != 0:
        newOddList.append(i)
    else:
        continue

for i in newOddList:
    print(i)
