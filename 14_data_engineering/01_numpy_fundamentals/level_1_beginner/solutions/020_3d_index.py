"""
Exercise 020: 3D Index
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    result = np.unravel_index(99, (6, 7, 8))
    return result
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
