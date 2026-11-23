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
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(3, 4)
        rows = arr[1, :]
        cols = arr[:, 2]
        print("Rows : ", rows)
        print("Cols : ", cols)

    # 7
    def customArray():
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(3, 4)
        return arr

    # 8
    def extractFirstTwoRows():
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(3, 4)

        rows = arr[:2, :]
        return rows

    # 9
    def extractLastTwoColumn():
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(3, 4)
        cols = arr[:, -1:2]
        return cols

    # 10
    def reverseArray():
        arr = np.array([1, 2, 3, 4, 5, 6])
        return arr.flip

    # 11
    def flattenArray():
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(3, 3)
        return arr.flatten

    # 12
    def transposingArray():
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(3, 4)
        b = arr.T
        print("After transpose the new shape : ", b.shape())


class MathsOperation(Solution):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[1, 0], [1, 2]])
         def arithmeticOperation():
      