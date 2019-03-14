class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return True
            if lo != mid and nums[lo] == nums[mid]:
                lo = mid
                continue
            if hi != mid and nums[hi] == nums[mid]:
                hi = mid
                continue
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (
                    target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid

        return target in nums[lo:lo + 1]

    def solution(self, nums, target):
        if not nums:
            return False

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                r -= 1

        return False


print(Solution().search([1,3,1,1,1,1], 3))
