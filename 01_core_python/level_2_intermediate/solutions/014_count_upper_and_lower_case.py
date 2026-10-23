"""Exercise 014 — Count Upper and Lower Case.

Count uppercase and lowercase letters in a sentence.
"""

# Your implementation here
pass

sentence = input("Enter any sentence :- ")
uCounter = 0
lCounter = 0
for i in sentence:
    if i.isupper():
        uCounter += 1
    elif i.islower():
        lCounter += 1
    else:
        continue

print("Upper case alphabets : ", uCounter)
print("Lower case alphabets : ", lCounter)
