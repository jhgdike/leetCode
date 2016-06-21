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
        return self.countNumbersWithUniqueDigits(n-1) + 9 * self.a_list(9, n-1)

    def a_list(self, n, m):
        a = 1
        for i in range(0, m):
            a = a * (n-i)
        return a
