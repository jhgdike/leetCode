class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_len = 1
        this_len = 1
        for i in range(1, len(nums)):
            if nums[i - 1] <= nums[i]:
                this_len += 1
            else:
                if longest_len < this_len:
                    longest_len = this_len
                this_len = 1
        if longest_len < this_len:
            longest_len = this_len
        return longest_len
