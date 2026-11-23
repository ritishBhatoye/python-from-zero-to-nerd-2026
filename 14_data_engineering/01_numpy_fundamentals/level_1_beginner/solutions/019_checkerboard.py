"""
Exercise 019: Checkerboard
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    a = np.zeros((8, 8))
    a[1::2, ::2] = 1
    a[::2, 1::2] = 1
    return a
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
