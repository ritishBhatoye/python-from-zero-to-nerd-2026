"""Exercise 097 — Reverse String.

Print string in reverse order.
"""

# Your implementation here
pass


def reverseStr(n):
    ans = []
    n = list(n)

    j = len(n) - 1

    while j != 0:
        ans += n[j]
        j -= 1
    return "".join(n)


n = input("Enter the string: ")
print("Reverse string:", reverseStr(n))
