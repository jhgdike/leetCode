class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = cur_end = cur_far = 0
        for i in range(len(nums) - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = cur_far
        return jumps
