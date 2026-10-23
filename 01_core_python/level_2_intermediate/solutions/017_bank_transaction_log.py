"""Exercise 017 — Bank Transaction Log.

Compute net amount from transaction log (D=deposit, W=withdrawal).
"""

# Your implementation here
pass


def bankTransaction(d=[], w=[]):
    dSum = 0
    wSum = 0
    ans = 0
    for x in d:
        dSum += x

    for x in w:
        wSum += x

    if dSum > wSum:
        ans = dSum - wSum
    else:
        ans = wSum - dSum

    return ans


d = [300, 300, 100]
w = [200]

print("Bank Transaction : ", bankTransaction(d, w))
