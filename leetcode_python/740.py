class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = [0] * 10001
        for num in nums:
            vals[num] += num
        tip, skip = 0, 0
        for i in range(1, 10001):
            tmp = tip
            tip = skip + vals[i]
            skip = max(tmp, skip)
        return max(tip, skip)


Solution().deleteAndEarn([8,10,4,9,1,3,5,9,4,10])
