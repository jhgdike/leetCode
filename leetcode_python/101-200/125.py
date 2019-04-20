class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while True:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i >= j:
                return True
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1


"""
class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(filter(str.isalnum,str(s))).lower()
        return s==s[::-1]
"""
