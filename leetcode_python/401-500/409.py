from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        single = False
        res = 0
        for char in c.values():
            if char & 1:
                single = True
                res += char - 1
            else:
                res += char
        if single:
            res += 1
        return res
