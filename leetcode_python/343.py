class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        if n == 3:
            return 2
        while n >= 5:
            res *= 3
            n -= 3
        if n == 4:
            res *= 4
        elif res > 1:
            res *= n
        return res
