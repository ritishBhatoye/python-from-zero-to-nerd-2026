"""Exercise 013 — Count Letters and Digits.

Calculate number of letters and digits in a sentence.
"""


# Your implementation here

sentence = input("Enter the sentence : ")

sCounter = 0
dCounter = 0
for i in sentence:
    if i.isalpha():
        sCounter += 1
    elif i.isdigit():
        dCounter += 1
    else:
        continue

print("Alphabets : ", sCounter)
print("Digits : ", dCounter)
