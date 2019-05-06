class Solution(object):
    fib_list = [0] * 31

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N in (1, 2):
            return 1
        p, pp = 0, 1
        for i in range(1, N):
            p, pp = pp, pp + p
        return pp
