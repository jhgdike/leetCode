class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if s[i+1] == s[j]:
                    if self.valid(s, i+2, j -1):
                        return True
                if s[i] == s[j-1]:
                    if self.valid(s, i+1, j-2):
                        return True
                return False
            i += 1
            j -= 1
        return True

    def valid(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
