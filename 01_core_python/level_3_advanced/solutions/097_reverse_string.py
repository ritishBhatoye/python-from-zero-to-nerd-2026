"""Exercise 097 — Reverse String.

Print string in reverse order.
"""

# Your implementation here
pass


def swap(a, b):
    return b, a


def reverseStr(n):
    i = 0
    j = len(n) - 1

    while i < j:
        n[i], n[j] = swap(n[i], n[j])
        i += 1
        j -= 1

    return n


n = input("Enter the string : ")
print("Reverse string :- ", reverseStr(n))
