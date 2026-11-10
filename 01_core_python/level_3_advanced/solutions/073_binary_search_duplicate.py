"""Exercise 073 — Binary Search Duplicate.

Implement binary search function (duplicate question).
"""

# Your implementation here
pass

arr = [1, 2, 2, 2, 3, 4]


def bs(x):
    s = 0
    e = len(arr) - 1
    startingID = 0
    endingID = 0
    ans = []
    while s <= e:
        mid = int((s + e) / 2)

        if arr[mid] == x:
            endingID = mid
            s = mid - 1
        elif arr[mid] < x:
            e = mid + 1
        else:
            s = mid - 1

    ans.append(startingID)

    s = 0
    e = len(arr) - 1

    while s <= e:
        mid = int((s + e) / 2)

        if arr[mid] == x:
            endingID = mid
            e = mid + 1
        elif arr[mid] < x:
            e = mid + 1
        else:
            s = mid - 1

    ans.append(endingID)

    return ans


x = int(input("Enter the number you want to search : "))
print("Binary Search Indices for ", x, " :- ", bs(x))
