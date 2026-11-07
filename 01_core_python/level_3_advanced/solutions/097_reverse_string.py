"""Exercise 097 — Reverse String.

Print string in reverse order.
"""

# Your implementation here
pass


def reverseStr(n):
    i = 0
    j = len(n) - 1

    while i < j:
        swap(n[i], n[j])
        i += 1
        j -= 1

    return n
