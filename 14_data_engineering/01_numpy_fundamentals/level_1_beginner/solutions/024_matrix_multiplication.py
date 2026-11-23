"""
Exercise 024: Matrix Multiplication
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    a = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15],
        ]
    )
    b = np.array(
        [
            [16, 17, 18],
            [19, 20, 21],
            [22, 23, 24],
        ]
    )
    result = np.matmul(a, b)
    return result
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
