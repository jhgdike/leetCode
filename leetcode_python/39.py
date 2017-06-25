class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.lengh = len(candidates)
        self.dfs(candidates, 0, [], target, res)
        return res

    def dfs(self, nums, i, arr, target, res):
        if i >= self.lengh:
            return
        if target <= 0:
            if target == 0:
                res.append(list(arr))
        else:
            arr.append(nums[i])
            self.dfs(nums, i, arr, target - nums[i], res)
            arr.pop()
            self.dfs(nums, i + 1, arr, target, res)