class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0] * len(s) for _ in range(len(s))]

        count = len(s)
        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(1, len(s)):
            for j in range(len(s) - i):
                x = j
                y = j + i
                if i == 1:
                    if s[x] == s[y]:
                        dp[x][y] = 1
                        count += 1
                else:
                    if s[x] == s[y] and dp[x + 1][y - 1]:
                        dp[x][y] = 1
                        count += 1
        return count


class Solution2(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = len(s)
        i, j = 0, 0
        while i < l:
            j = i
            while j < l and s[j] == s[i]: j += 1
            res += (j - i + 1) * (j - i) // 2
            left, right = i - 1, j
            while left >= 0 and right < l and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            i = j
        return res


class Solution3(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 1
        for i in range(1, len(s)):
            # 以i为中心进行扩展
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            # 以i-1和i为中心进行扩展
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res
