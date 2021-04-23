class Solution(object):

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        total = res = 0
        while r < len(nums):
            if nums[r] == target:
                return 1
            total += nums[r]
            r += 1
            while total >= target:
                total -= nums[l]
                l += 1
                if res:
                    res = min(res, r - l + 1)
                else:
                    res = r - l + 1
        return res

    def minSubArrayLen22(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                dp[j] += nums[j + i]
                if dp[j] >= target:
                    return i + 1
        return 0


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(4, [1, 4, 4]))
print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
