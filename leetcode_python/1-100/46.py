from itertools import permutations


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in permutations(nums):
            res.append(list(i))
        return res
