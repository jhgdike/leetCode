class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up+1
        return max(up, down)


print(Solution().wiggleMaxLength([1,7,4,9,2,5]))
print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
