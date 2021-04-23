class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        def dfs(i):
            if i > n:
                return
            res.append(i)
            for j in range(10):
                dfs(i*10+j)
        for i in range(1, 10):
            dfs(i)
        return res


print(Solution().lexicalOrder(111))
# for i in range(1,100):
#     print(Solution().lexicalOrder(i))


