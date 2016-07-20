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
        result = [-1, -1]
        # normal_search(nums, target, result)
        better_search(nums, target, result)
        return [-1, -1] if result[0] > result[1] else result


def normal_search(nums, target, result):
    for i, v in enumerate(nums):
        if v < target:
            result[0] = i + 1
        elif v > target:
            result[1] = i - 1
            break


def better_search(nums, target, result):
    length = len(nums) - 1
    left, right = 0, length
    while left < right:
        mid = (left + right) / 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    result[0] = left
    left, right = 0, length
    while left < right:
        mid = (left + right) / 2 + 1
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid
    result[1] = right
