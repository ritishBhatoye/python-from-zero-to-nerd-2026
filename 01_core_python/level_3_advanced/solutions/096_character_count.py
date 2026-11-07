"""Exercise 096 — Character Count.

Count and print frequency of each character.
"""


# Your implementation here


def chrCount(n):
    ans = {}
    n = list(n)
    for i in range(len(n)):
        if n[i] in ans:
            ans[n[i]] += 1
        else:
            ans[n[i]] = 1
    return ans


n = input("Enter string : ")
print("Character count : ", chrCount(n))
