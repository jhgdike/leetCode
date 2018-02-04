class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        far = 0
        for i in range(len(nums)):
            if far >= len(nums) - 1:
                return True
            if far < i or far == i and nums[i] == 0:
                return False
            far = max(far, i + nums[i])
