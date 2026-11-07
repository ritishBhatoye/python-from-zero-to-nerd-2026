"""Exercise 059 — Extract Email Company.

Extract company name from email address using regex.
"""

# Your implementation here
pass


def extractCompany(n):
    ans = ""

    i = 0
    while(n[i]!="@"):
        i++

    return ans


n = input("Enter extract company : ")
print("Extracted Company Name : ", extractCompany(n))
