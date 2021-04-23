class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1
        for sum_ in range(1, target+1):
            for x in nums:
                if x <= sum_:
                    dp[sum_] += dp[sum_-x]
        return dp[target]


print(Solution().combinationSum4([1, 2, 3], 4))
print(Solution().combinationSum4([3, 1, 2, 4], 4))
print(Solution().combinationSum4([4,2,1], 32))
