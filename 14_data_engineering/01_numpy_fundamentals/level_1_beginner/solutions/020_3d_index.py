"""
Exercise 020: 3D Index
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    result = np.unravel_index(5, (2, 3, 4))
    return result
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
