"""Exercise 060 — Extract Digits from String.

Extract only digit sequences from input string.
"""

# Your implementation here
pass


def extractDigitsFromSt(n):
    ans = ""
    for i in range(len(n)):
        if n[i].isalpha():
            i += 1
        else:
            ans += n[i]

    return ans


n = input("Enter the digits : ")
print("Extract Digits from String : ", extractDigitsFromSt(n))
