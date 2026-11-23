"""
Exercise 022: Normalize Matrix
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    a = np.random.random((5, 5))

    minimum = np.min(a)
    maximum = np.max(a)

    normalized = (a - minimum) / maximum - minimum
    return normalized
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
