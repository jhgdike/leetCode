class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        hset = set(nums)
        for i in range(length):
            sec = target - nums[i]
            if sec in hset:
                for j in range(i+1, length):
                    if nums[j] == sec:
                        return [i, j]
