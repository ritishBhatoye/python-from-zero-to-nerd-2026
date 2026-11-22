"""
Exercise 013: Random Min Max
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    a = np.random.rand(4, 2)
    print("Min : ", np.min(a))
    print("Max : ", np.max(a))
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
