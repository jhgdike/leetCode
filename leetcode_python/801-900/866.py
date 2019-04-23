"""
python代码 用到下述两个定理 数学规律1：除 11 外的偶数位回文数，都能被 11 整除 数学规律2：除 2 和 3 外，所有的素数一定在 6 的两侧

"""


class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        def judge_pri(n):  # 判断素数的很好的方式
            if n & 1 == 0:
                return False
            if (n + 1) % 6 != 0 and (n - 1) % 6 != 0:
                return False
            l, r = 3, n // 3
            while l <= r:
                if n % l == 0:
                    return False
                else:
                    l += 2
                    r = n // l
            return True

        def find_pal(num):
            res = str(num)
            n = len(res) // 2
            if res[n - 1::-1] >= res[n + 1:]:
                return int(res[:n + 1] + res[n - 1::-1])
            else:
                if res[n] != '9':
                    t = str(int(res[n]) + 1)
                    return int(res[:n] + t + res[n - 1::-1])
                else:
                    a = str(int(res[:n]) + 1)
                    if len(a) > n:
                        return 10 ** (2 * n + 1) + 1
                    else:
                        return int(a + '0' + a[::-1])

        if N == 1:
            return 2
        elif N < 4:
            return N
        elif N < 6:
            return 5
        elif N < 8:
            return 7
        elif N < 12:
            return 11
        K = len(str(N))
        if K % 2 == 0:
            # 偶数回文数一定不是素数，大于11的素数回文数一定是奇数。
            return self.primePalindrome(10 ** K + 1)
        else:
            res = find_pal(N)
            if judge_pri(res):
                return res
            else:
                return self.primePalindrome(res + 1)
