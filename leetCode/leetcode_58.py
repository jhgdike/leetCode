class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = lengh = 0
        for ch in s:
            if ch == ' ':
               lengh, last = 0, lengh or last
            else:
                lengh += 1
        return lengh or last
