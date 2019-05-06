class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = ''.join(reversed(s))

        count = len(s)
        while count > 0:
            if rs[-count:] == s[:count]:
                break
            count -= 1
        return str(rs[:len(s) -count] + s)
