class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n_sum = sum(nums)

        def sub_set(nums, ss):
            dp = [1] + [0] * ss
            for n in nums:
                for i in range(ss, n-1, -1):
                    dp[i] += dp[i-n]
            return dp[ss]
        return 0 if n_sum < S or (S+n_sum) % 2 else sub_set(nums, (S+n_sum)>>1)
