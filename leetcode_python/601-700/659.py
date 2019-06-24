class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dd = dict()
        d_cnt = dict()
        for num in nums:
            d_cnt[num] = d_cnt.get(num, 0) + 1

        for num in nums:
            if d_cnt[num] == 0:
                continue
            d_cnt[num] -= 1
            if dd.get(num - 1, 0) > 0:
                dd[num - 1] -= 1
                dd[num] = dd.get(num, 0) + 1
            elif d_cnt.get(num + 1) and d_cnt.get(num + 2):
                d_cnt[num + 1] -= 1
                d_cnt[num + 2] -= 1
                dd[num + 2] = dd.get(num + 2, 0) + 1
            else:
                return False
        return True

