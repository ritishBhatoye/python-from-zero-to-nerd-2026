"""
Exercise 008: Reverse Vector
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    a = np.array([1, 2, 3, 4, 5, 6])
    b = np.flip(a)
    print(b)
    print("Alternative : ", a)
    # Alternative
    a[::-1]
    print("Alternative : ", a)
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
