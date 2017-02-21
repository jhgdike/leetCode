class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = False
        min_num = None
        last_sum = cur_sum = max_sum = 0
        for num in nums:
            if num < 0:
                max_sum = max(last_sum, cur_sum, max_sum)
                if cur_sum > last_sum:
                    last_sum = cur_sum
                cur_sum, last_sum = 0, num + last_sum
            else:
                cur_sum += num
                last_sum += num
                pos = True
            if min_num is None or min_num < num:
                min_num = num
        if not pos:
            return min_num
        return max(last_sum, cur_sum, max_sum, nums[-1])
