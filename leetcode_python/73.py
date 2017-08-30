class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        first_row = None
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    first_row = i
                    break
            if first_row is not None:
                break
        if first_row is None:
            return

        for i in range(first_row + 1, M):
            this_row = False
            for j in range(N):
                if matrix[i][j] == 0:
                    this_row = True
                    matrix[first_row][j] = 0

            if this_row:
                for j in range(N):
                    matrix[i][j] = 0

        for i in range(N):
            if matrix[first_row][i] == 0:
                for j in range(M):
                    matrix[j][i] = 0

        for i in range(N):
            matrix[first_row][i] = 0

Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])