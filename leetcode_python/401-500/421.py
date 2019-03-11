class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(31, -1, -1):
            res <<= 1
            prefix = {num >> i for num in nums}
            # res = p ^ q. res ^ p = q. | res ^ p should be sure that
            # in the rest of prefix and end of number is 1
            res += any([res ^ 1 ^ p in prefix for p in prefix])
        return res


def test():
    nums = [3, 10, 5, 25, 2, 8]
    return Solution().findMaximumXOR(nums)
