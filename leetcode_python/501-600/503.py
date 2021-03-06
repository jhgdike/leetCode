class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[i % N] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % N]
            stack.append(i % N)
        return res
