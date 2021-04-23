class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        snum = sorted(nums)
        n = len(nums)
        for i in range(1, len(nums), 2):
            nums[i] = snum[n-1]
            n -= 1
        for i in range(0, len(nums), 2):
            nums[i] = snum[n-1]
            n -= 1
        return nums


print(Solution().wiggleSort([1,5,1,1,6,4]))
print(Solution().wiggleSort([1,3,2,2,3,1]))
print(Solution().wiggleSort([]))
print(Solution().wiggleSort([]))
print(Solution().wiggleSort([]))
print(Solution().wiggleSort([]))
print(Solution().wiggleSort([]))
