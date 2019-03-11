class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def count(s):
            a, b = 0, 0
            for x in s:
                if x == '0':
                    a += 1
                else:
                    b += 1
            return a, b
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            a, b = count(s)
            for i in range(m, a-1, -1):
                for j in range(n, b-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-a][j-b] + 1)
        return dp[m][n]
