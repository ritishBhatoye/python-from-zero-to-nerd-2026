"""
Exercise 021: Tile Checkerboard
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    a = np.identity(2)
    np.tile(a, (6, 6))
    return a
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
