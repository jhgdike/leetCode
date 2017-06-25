class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        left, right, height = [0] * n, [n] * n, [0] * n
        max_sum = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j + 1

                if matrix[i][n-j-1] == '1':
                    right[n-j-1] = min(right[n-j-1], cur_right)
                else:
                    right[n-j-1] = n
                    cur_right = n-j-1

            for j in range(n):
                s_e = min(right[j] - left[j], height[j])
                max_sum = max(max_sum, s_e * s_e)
        return max_sum


class Solution2(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min((dp[i-1][j], dp[i][j-1], dp[i-1][j-1])) + 1
                    res = max(res, dp[i][j])
        return res * res
