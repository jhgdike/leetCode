class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        high, length = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * length
        dp[0] = 1
        for i in range(high):
            for j in range(length):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[-1]
