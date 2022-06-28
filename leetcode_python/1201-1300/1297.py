import collections


class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        if minSize > len(s):
            return 0

        ans = dict()
        l, r = 0, minSize
        c = collections.Counter(s[:r])
        if len(c) <= maxLetters:
            ans[s[l:r]] = ans.get(s[l:r], 0) + 1
        while r < len(s):
            c[s[l]] -= 1
            if c[s[l]] == 0:
                c.pop(s[l])
            l += 1
            c[s[r]] += 1
            r += 1
            if len(c) <= maxLetters:
                ans[s[l:r]] = ans.get(s[l:r], 0) + 1
        return 0 if not ans else max(ans.values())


print(Solution().maxFreq("aababcaab", 2, 3, 4))
