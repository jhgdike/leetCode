class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n_sum = sum(nums)
        if n_sum % 2:
            return False
        ss = n_sum >> 1
        dp = {0}
        cache = [0]
        for n in nums:
            if ss-n in dp:
                return True
            for i in range(len(cache)):
                tt = cache[i] + n
                cache.append(tt)
                dp.add(tt)
        return False
