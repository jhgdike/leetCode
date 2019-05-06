class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = [1, i, i]
            else:
                d[n][0] += 1
                d[n][2] = i
        max_count, min_len = 0, 0
        for val in d.values():
            if val[0] > max_count:
                max_count = val[0]
                min_len = val[2] - val[1] + 1
            elif val[0] == max_count:
                min_len = min(min_len, val[2] - val[1] + 1)
        return min_len
