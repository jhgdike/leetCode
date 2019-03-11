class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 1:
            return False
        d = {}
        w = t + 1
        for i, v in enumerate(nums):
            m = v // w
            if m in d:
                return True
            if m-1 in d and v-d[m-1] < w:
                return True
            if m+1 in d and d[m+1]-v < w:
                return True
            d[m] = v
            if i >= k:
                tmp = nums[i-k] // w
                if tmp in d:
                    del d[tmp]
        return False


print(Solution().containsNearbyAlmostDuplicate([2, 0, -2, 2], 2, 1))
