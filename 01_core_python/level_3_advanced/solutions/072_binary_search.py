"""Exercise 072 — Binary Search.

Implement binary search function.
"""

# Your implementation here
pass


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def bs(k):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = int((s + e) / 2)
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            s = mid + 1
        else:
            e = mid - 1


k = int(input("Enter the element you want to search : "))

print("Answer :- ", bs(k))
