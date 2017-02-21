class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x and x % 10 == 0):
            return False
        return str(x) == ''.join(reversed(str(x)))
