"""Exercise 007 — 2D Array Generator.

Generate 2D array where element[i][j] = i*j. Input: dimensions as X,Y
"""

# Your implementation here
pass


rows = int(input("Enter the row : "))
cols = int(input("Enter the column : "))

ans = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * j)
    ans.append(row)

print(ans)
