class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = max_mul = min_mul = nums[0]
        for i in range(1, len(nums)):
            a, b = nums[i] * max_mul, nums[i] * min_mul
            max_mul, min_mul = max((a, b, nums[i])), min((a, b, nums[i]))
            res = max(res, max_mul)
        return res
