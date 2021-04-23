class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def dfs(ss, cur):
            if ss == ss[::-1]:
                res.append(cur + [ss])
            for i in range(1, len(ss)):
                if ss[:i] == ss[:i][::-1]:
                    dfs(ss[i:], cur + [ss[:i]])
        dfs(s, [])
        return res

    def test(self, s):
        """动态规划加回溯"""
        dp = [[True]*len(s) for _ in range(len(s))]
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        res = []
        ans = []
        n = len(s)

        def dfs(i):
            if i == n:
                res.append(ans[:])
                return
            for j in range(i, n):
                if dp[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()
        dfs(0)
        return res

    def test2(self, s):
        """动态规划加回溯的优化，记忆化搜索"""
        dp = [[0] * len(s) for _ in range(len(s))]
        def is_palindrome(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            if i>=j:
                dp[i][j] = 1
                return 1
            dp[i][j] = (s[i] == s[j] and is_palindrome(i+1,j-1) and 1) or -1
            return dp[i][j]
        res = []
        ans = []
        n = len(s)

        def dfs(i):
            if i == n:
                res.append(ans[:])
                return
            for j in range(i, n):
                if is_palindrome(i, j) == 1:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return res
