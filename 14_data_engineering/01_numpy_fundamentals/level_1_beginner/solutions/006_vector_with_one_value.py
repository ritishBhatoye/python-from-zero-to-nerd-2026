"""
Exercise 006: Vector with One Value
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    a = np.zeros((2, 2))
    a[0, 1] = 99
    print(a)


if __name__ == "__main__":
    result = solution()
    print(result)
