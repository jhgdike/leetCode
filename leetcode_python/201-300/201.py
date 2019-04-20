class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return m << count


def test():
    import time
    import random
    for i in range(100):
        m = random.randint(0, 2147483647)
        n = random.randint(m, 2147483647)
        start_time = time.time()

        res = Solution().rangeBitwiseAnd(m, n)
        print('m,n: {},{}. latency: {}, res: {}'.format(m, n, time.time() - start_time, res))
        # time.sleep(0.1)


test()
