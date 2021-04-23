class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [1] + [0] * n
        primes = [0] * len(primes)
        for i in range(1, n):
            dp[i] = min(dp[primes[j]] * primes[j] for j in range(len(primes)))


class Solution2:
    def nthSuperUglyNumber(self, n, primes):
        dp = [1] + [0] * (n - 1)
        l = len(primes)
        primIdxs = [0] * l  # 记录上一个最大值在每个质数上累加了多少次
        for i in range(1, n):
            min = min_index = None
            for j in range(l):
                cur = dp[primIdxs[j]] * primes[j]
                if not min or cur < min:
                    min, min_index = cur, j
            dp[i] = min
            primIdxs[min_index] += 1
        return dp[-1]


class Solution3:
    def nthSuperUglyNumber(self, n, primes):
        dp=[1]+[0]*(n-1)
        l=len(primes)
        primIdxs=[0]*l #记录上一个最大值在每个质数上累加了多少次
        for i in range(1,n):
            dp[i]=min(dp[primIdxs[j]]*primes[j]for j in range(l))
            for j in range(l):
                if dp[i]>=dp[primIdxs[j]]*primes[j]:primIdxs[j]+=1
        return dp[-1]


s = Solution3()

print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))
