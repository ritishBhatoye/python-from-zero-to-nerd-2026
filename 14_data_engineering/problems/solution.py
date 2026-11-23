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
        print("Size of array : ", arr.size)
        print("Shape of array : ", arr.shape)
        print("Dimension of array : ", arr.ndim)
        print("Type of array : ", arr.dtype)

    # 4
    def arrCreationWithRes():
        zArr = np.zeros(4, 4)

        print("Zeros array : ", zArr)
        oArr = np.ones(4, 4)
        print("Ones array : ", oArr)
        iArr = np.identity(4, 4)
        print("Identity array : ", iArr)

    # 5
    def genArrFrom0to10():
        gArray = np.linespace(0, 10, 20)
        print(gArray)

    # 6
    def extractingRowNCol():
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]).reshape(
            3, 4
        )
        print(arr)
