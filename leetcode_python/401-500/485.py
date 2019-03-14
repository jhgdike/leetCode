class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cur = 0
        for i in nums:
            if i == 0:
                res = max(res, cur)
                cur = 0
            else:
                cur += 1
        return max(cur, res)
