"""Exercise 016 — Filter Odd Numbers.

Use list comprehension to filter odd numbers from comma-separated input.
"""

# Your implementation here
pass

odd = []
n = int(input("Enter limit : "))

for i in range(0, n):
    num = int(input("Enter the number : "))
    odd.append(num)

newOddList = []


for i in odd:
    if i % 2 != 0:
        newOddList.append(i)
    else:
        continue

for i in newOddList:
    print(i)
