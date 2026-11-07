"""Exercise 059 — Extract Email Company.

Extract company name from email address using regex.
"""

# Your implementation here
pass


def extractCompany(n):
    ans = ""
    for i in range(len(n)):
        if n[i] == "@":
            break
        else:
            ans += n[i]

    return ans


n = input("Enter extract company : ")
print("Extracted Company Name : ", extractCompany(n))
