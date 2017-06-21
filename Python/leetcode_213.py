class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _rob_range(nums, i, j):
            last = now = 0
            for x in range(i, j):
                last, now = now, max(now, last + nums[x])
            return now

        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        return max(_rob_range(nums, 0, len(nums)-1), _rob_range(nums, 1, len(nums)))
