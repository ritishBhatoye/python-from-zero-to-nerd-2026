"""Exercise 010 — Remove Duplicates and Sort.

Remove duplicate words and sort alphanumerically.
"""

# Your implementation here
pass


lines = input("Enter the line : ")

words = lines.split(",")
words.sort()
for w in words:
    w = int(w)
    if words[w] == words[w + 1]:
        words.pop(w)

print(words)
