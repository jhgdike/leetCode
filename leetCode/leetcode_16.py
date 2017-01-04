class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                lo, hi = i + 1, len(nums) - 1,
                while lo < hi:
                    sm = nums[lo] + nums[hi] + nums[i]
                    if sm == target:
                        return sm
                    else:
                        if abs(sm - target) < abs(res - target):
                            res = sm

                        if sm < target:
                            lo += 1
                        else:
                            hi -= 1
        return res
