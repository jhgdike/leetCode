class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                if i == len(s):
                    return True
            else:
                j += 1
        return False
