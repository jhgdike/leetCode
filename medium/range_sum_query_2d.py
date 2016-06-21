# coding: utf-8


class NumMatrix(object):

    def __init__(self, matrix):
        """

        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        row = len(matrix)
        if row:
            col = len(matrix[0])
            for i in range(0, row):
                for j in range(0, col):
                    if i > 0 and j > 0:
                        matrix[i][j] = matrix[i][j-1] + matrix[i-1][j] + matrix[i][j] - matrix[i-1][j-1]
                    if i == 0 and j > 0:
                        matrix[i][j] = matrix[i][j-1] + matrix[i][j]
                    elif j == 0 and i > 0:
                        matrix[i][j] = matrix[i-1][j] + matrix[i][j]
            self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix:
            return 0
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        if row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        if col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]
