import numpy as np


class Solution:
    # 1
    def arrCreation():
        a = np.arange((1, 21))
        return a

    # 2
    def cubicMatrix():
        arr = np.arange(1, 21).reshape(3, 3)
        return arr

    # 3
    def arrMethods():
        arr = np.array(
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
            ]
        )
