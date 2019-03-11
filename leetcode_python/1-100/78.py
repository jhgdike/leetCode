class Solution(object):

    def subsets(self, nums):
        return self.lazy_solution_subsets(nums)

    def lazy_solution_subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations
        res = []
        for i in range(len(nums)+1):
            for p in combinations(nums, i):
                res.append(p)
        return res

    def subsets_1(self, nums):
        res = []
        n, com = len(nums), 2 ** len(nums)
        for i in range(com):
            tmp, j = [], 1
            for j in range(0, n):
                if i & (2 ** j):
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    def subsets_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]

        for val in nums:
            temp = [item + [val] for item in ret]
            ret.extend(temp)

        return ret
