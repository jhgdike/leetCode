from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp))
        return ''.join(nums) if nums[0] != '0' else '0'


def cmp(a, b):
    if a == b:
        return 0
    elif a + b < b + a:
        return 1
    else:
        return -1


print(Solution().largestNumber([3, 30, 34, 5, 9]))
