"""Exercise 022 — Word Frequency Counter.

Compute and print word frequency, sorted alphabetically.
"""

# Your implementation here
pass

sentence = input("Enter the sentence :- ")
sentence = sentence.lower()
senList = sentence.split()


ans = {}
for i in senList:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1


print(ans)
