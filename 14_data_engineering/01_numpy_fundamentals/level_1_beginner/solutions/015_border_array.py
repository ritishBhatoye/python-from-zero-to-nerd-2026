"""
Exercise 015: Border Array
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    a = np.ones((5, 5))
    b = np.pad(a, pad_width=1, mode="constant", constant_values=0)

    return b
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
