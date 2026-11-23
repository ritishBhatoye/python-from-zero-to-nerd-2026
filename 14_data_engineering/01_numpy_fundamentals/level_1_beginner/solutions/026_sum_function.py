"""
Exercise 026: Sum Function
"""

import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    a = np.sum(np.arrange(5)) - 1
    print("With numpy : ",a)
      b = sum(range(5), - 1)
    print("Without numpy : ",b)
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
