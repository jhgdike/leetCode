class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0] * len(piles) for _ in range(len(piles))]
        for i in range(len(piles) - 1, -1, -1):
            dp[i][i] = piles[i]
            for j in range(i + 1, len(piles)):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][-1] > 0
