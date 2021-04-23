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


class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])
        k = min(m, n)
        ans = []
        for loop in range(0, (k+1)//2):
            for i in range(loop, m-loop): ans.append(matrix[loop][i])
            for i in range(loop+1, n-loop-1): ans.append(matrix[i][m-loop-1])
            if n - loop - 1 != loop:
                for i in range(m-loop-1, loop-1, -1):
                    ans.append(matrix[n-loop-1][i])
            if m-loop-1 != loop:
                for i in range(n-loop-2, loop, -1):
                    ans.append(matrix[i][loop])
        return ans


print(Solution2().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution2().spiralOrder([[7],[9],[6]]))
