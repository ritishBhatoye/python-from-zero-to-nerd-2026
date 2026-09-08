"""Exercise 031 — Maximum Length String.

Print the string with maximum length. If equal, print both.
"""

# Your implementation here
pass


def maxLenStr(s1, s2):
    if len(s1) > len(s2):
        return s1
    elif len(s1) == len(s2):
        print(s1)
        print(s2)
        return ""
    else:
        return s2


s1 = input("Enter the string one : ")
s2 = input("Enter the string two : ")

print("Maximum string is :- ", maxLenStr(s1, s2))
