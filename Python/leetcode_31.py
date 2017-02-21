class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sp = 0
        if len(nums) <= 1:
            return
        for i in range(1, len(nums)):
            if nums[-i] > nums[-(i+1)]:
                sp = len(nums) - i
                break
        if sp != 0:
            sw = sp
            while sw < len(nums) - 1:  #: find the index of the sub number
                if nums[sw+1] <= nums[sp-1]:
                    break
                sw += 1
            nums[sw], nums[sp-1] = nums[sp-1], nums[sw]
        for i in range(1, (len(nums)-sp+2)/2):
            nums[sp+i-1], nums[-i] = nums[-i], nums[sp+i-1]
