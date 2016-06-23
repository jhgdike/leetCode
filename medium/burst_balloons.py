# coding: utf-8


class Solution(object):
    """
    dp solution
    References: https://leetcode.com/discuss/72216/share-some-analysis-and-explanations
    """
    def maxCoins(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                for i in xrange(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] +
                                          dp[left][i] + dp[i][right])
        return dp[0][n - 1]
