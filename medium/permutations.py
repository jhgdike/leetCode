# coding: utf-8


class Permutation(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        while True:
            if not nums:
                break
            res.append(nums[:])
            nums = self.next_permutation(nums)
        return res

    def next_permutation(self, nums):
        j = last = len(nums) - 1
        while last > 0:
            if nums[last - 1] < nums[last]:
                break
            last -= 1
        if not last:
            return False
        while j > 0:
            if nums[j] > nums[last - 1]:
                nums[j], nums[last - 1] = nums[last - 1], nums[j]
                break
            j -= 1
        res, tail = nums[:last], nums[last:]
        tail.reverse()
        res.extend(tail)
        return res
