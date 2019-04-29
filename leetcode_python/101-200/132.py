class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0
        dp = [[0] * n for _ in range(n)]
        dp2 = [-1] * (n+1)
        for i in range(n-1, -1, -1):
            dp2[i] = dp2[i+1] + 1
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    dp2[i] = min(dp2[j + 1] + 1, dp2[i])

        return dp2[0]


print(Solution().minCut('ab'))
