"""rikimberley's solution for python"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        max_n = nums[-1]
        if 4 * nums[0] > target or 4 * nums[-1] < target:
            return res
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i-1]:
                continue
            if x + 3 * max_n < target:
                continue
            if 4 * x > target:
                break
            if 4 * x == target and i + 3 < len(nums) and nums[i+3] == x:
                res.append([x] * 4)
                break
            self.threesum_for_foursum(nums, target - x, i + 1, len(nums) - 1, res, x)
        return res

    def threesum_for_foursum(self, nums, target, low, high, res, item):
        if low + 1 >= high:
            return
        if 3 * nums[low] > target or 3 * nums[-1] < target:
            return
        for i in range(low, high - 1):
            z = nums[i]
            if i > low and z == nums[i - 1]:
                continue
            if z + 2 * nums[high] < target:
                continue
            if 3 * nums[i] > target:
                break
            if 3 * nums[i] == target and i + 1 < high and z == nums[i + 2]:
                res.append([item] + [z] * 3)
                break
            self.twosum_for_foursum(nums, target - z, i + 1, high, res, item, z)

    def twosum_for_foursum(self, nums, target, low, high, res, item1, item2):
        if low >= high:
            return
        if 2 * nums[low] > target or 2 * nums[high] < target:
            return
        i, j = low, high
        while i < j:
            sum_n = nums[i] + nums[j]
            if target == sum_n:
                res.append([item1, item2, nums[i], nums[j]])

                x = nums[i]
                while i < j and x == nums[i]:
                    i += 1
                x = nums[j]
                while i < j and x == nums[j]:
                    j -= 1

            if sum_n < target:
                i += 1
            if sum_n > target:
                j -= 1
Solution().fourSum([0,1,5,0,1,5,5,-4], 11)