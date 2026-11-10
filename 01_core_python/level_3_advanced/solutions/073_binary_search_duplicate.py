"""Exercise 073 — Binary Search Duplicate.

Implement binary search function (duplicate question).
"""


# Your implementation here
pass

arr = [1, 2, 2, 2, 3, 4]

def bs(x):
    s=0
    e=len(arr)-1
    ans = []
    while(s<=e):
        mid = int((s+e)/2)

        if(arr[mid]==x):
            s=mid-1
        elif(arr[mid]<x):
            e=mid+1
        else:
            s=mid-1

    ans.append(mid)

    s=0
    e=len(arr)-1

    while(s<=e):
        mid = int((s+e)/2)

        if(arr[mid]==x):
            