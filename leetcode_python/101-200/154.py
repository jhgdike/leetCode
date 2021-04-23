class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r = r - 1
        return nums[l]


class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def search(nums, l, r):
            while l < r:
                if nums[l] < nums[r - 1]:
                    return nums[l]
                if l + 5 >= r:
                    return min(nums[l:r])
                mid = (l + r) // 2
                if nums[mid] > nums[l]:
                    l = mid + 1
                elif nums[mid] < nums[l]:
                    r = mid + 1
                else:
                    return min(search(nums, l, mid) if l != mid else nums[l], search(nums, mid + 1, r))
            return nums[l]

        return search(nums, 0, len(nums))


s = Solution()
print(s.findMin([2, 1, 2, 2, 2]))
print(s.findMin([1, 3, 5]))
print(s.findMin([2, 2, 2, 0, 1]))
print(s.findMin([3, 1, 1]))
print(s.findMin([3, 1]))
print(s.findMin([2, 2, 2, 0, 2, 2]))
