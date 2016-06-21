# coding: utf-8


class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n > 10:
            return 0
        return self.countNumbersWithUniqueDigits(n-1) + 9 * reduce(lambda x, y: x * y, xrange(11-n,10))
