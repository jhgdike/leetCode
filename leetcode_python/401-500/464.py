class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= maxChoosableInteger:
            return True
        if maxChoosableInteger * (1+maxChoosableInteger)  >> 1 < desiredTotal:
            return False
        memo = {}
        def helper(nums, des):
            key = str(nums)
            if key in memo:
                return memo[key]

            if nums[-1] >= des:
                return True

            for i in range(len(nums)):
                if not helper(nums[:i] + nums[i+1:], des - nums[i]):
                    memo[key] = True
                    return True
            memo[key] = False
            return False
        return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
