"""Exercise 020 — Generator Divisible by 7.

Create generator that yields numbers divisible by 7 between 0 and n.
"""

# Your implementation here
pass

n = int(input("Enter the limit : "))


def generatorDivisibleBy7(x):
    for i in range(0, n):
        if i % 7 == 0:
            yield i
        else:
            continue


for num in generatorDivisibleBy7(n):
    print(num)
