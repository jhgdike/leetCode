class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = now = 0
        for num in nums:
            last, now = now, max(now, last + num)
        return now
