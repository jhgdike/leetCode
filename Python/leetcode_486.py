class Solution(object):
    """DP with less space"""
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [x for x in nums]
        for l in range(1, n):
            for i in range(n-l):
                dp[i] = max(nums[i] - dp[i+1], nums[i+l] - dp[i])
        return dp[0] >= 0


class Solution1(object):
    """DP"""
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0
