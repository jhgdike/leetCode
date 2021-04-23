class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ans = 0
        for num in nums:
            if num-1 in s:
                continue
            i = 1
            while True:
                if num+i in s:
                    i += 1
                else:
                    break
            ans = max(ans, i)
        return ans
