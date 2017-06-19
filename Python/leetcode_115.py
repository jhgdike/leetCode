class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[1] * (len(s) + 1)] + [[0 for _ in range(len(s) + 1)]for _ in range(len(t))]
        for i in range(len(t)):
            for j in range(0, len(s)):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i+1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[-1][-1]
