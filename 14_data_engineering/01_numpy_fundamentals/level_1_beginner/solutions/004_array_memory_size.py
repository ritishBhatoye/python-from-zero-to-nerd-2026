"""
Exercise 004: Array Memory Size
"""

import numpy as np


def solution():
    n = np.array([[1, 2, 3], [4, 5, 6]])
    print("N :- ", n)
    print("Size :- ", n.nbytes)
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
