class Solution(object):
    def __init__(self):
        self.temp = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        f = lambda k: (19-k) / 2 * k
        if n < k*(k+1)/2 or n > f(k):
            return []
        ans = []

        def dfs(cur, rest):
            if len(self.temp) == k and rest == 0:
                ans.append(self.temp[:])
                return
            if len(self.temp) + 10 - cur < k or rest <= 0:
                return
            dfs(cur+1, rest)
            self.temp.append(cur)
            dfs(cur+1, rest-cur)
            self.temp = self.temp[:len(self.temp)-1]

        dfs(1, n)
        return ans


print(Solution().combinationSum3(3, 7))
print(Solution().combinationSum3(3, 9))
