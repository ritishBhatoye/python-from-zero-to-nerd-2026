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
    b = np.tile(a, (4, 4))
    return b
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
