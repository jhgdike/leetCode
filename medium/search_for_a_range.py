# coding: utf-8


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        result = [0, len(nums)-1]
        for i, v in enumerate(nums):
            if v < target:
                result[0] = i + 1
            elif v > target:
                result[1] = i - 1
                break
        return [-1, -1] if result[0] > result[1] else result
