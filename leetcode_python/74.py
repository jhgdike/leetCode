class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        M, N = len(matrix), len(matrix[0])

        for i in range(M):
            if target <= matrix[i][N-1]:
                for j in range(N):
                    if matrix[i][N-j-1] == target:
                        return True
                else:
                    return False
        return False
