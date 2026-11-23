"""
Exercise 018: Diagonal Matrix
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    a = np.identity(5)
    a[1][1] = 2
    a[2][2] = 3
    a[3][3] = 4
    a[4][4] = 5

    return a
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
