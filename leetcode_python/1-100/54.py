class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        n = min(len(matrix), len(matrix[0]))
        for start in range(0, (n + 1) // 2):
            end_y = len(matrix) - start - 1
            end_x = len(matrix[0]) - start - 1

            for i in range(start, end_x + 1):
                res.append(matrix[start][i])
            for i in range(start, end_y):
                res.append(matrix[i + 1][end_x])
            if start < end_x and start < end_y:
                for i in range(end_x, start, -1):
                    res.append(matrix[end_y][i - 1])
            if start < end_x and start < end_y - 1:
                for i in range(end_y - 1, start, -1):
                    res.append(matrix[i][start])

        return res
