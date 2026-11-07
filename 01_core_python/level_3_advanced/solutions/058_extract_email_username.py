"""Exercise 058 — Extract Email Username.

Extract username from email address using regex.
"""

# Your implementation here
pass


def extractEmail(n):
    ans = ""
    for i in range(len(n)):
        if i == "@":
            break
        else:
            ans += n[i]

    return ans


n = input("Enter the email : ")
print("Extracted email ", extractEmail(n))
