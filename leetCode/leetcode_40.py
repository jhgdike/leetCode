class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, 0, target, res, [])
        return res

    def dfs(self, nums, index, target, res, arr):
        if target == 0:
            res.append(list(arr))
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                return
            if i and nums[i] == nums[i-1] and i > index:
                continue
            arr.append(nums[i])
            self.dfs(nums, i+1, target - nums[i], res, arr)
            arr.pop()