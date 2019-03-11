class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            max_sum = max(max_sum, nums[i], cur_sum)
        return max_sum
