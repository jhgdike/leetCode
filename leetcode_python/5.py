class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        start, max_len = 0, 1
        i = 0
        while i < len(s):
            if len(s) - i < max_len / 2:
                break
            j = k = i
            while k < len(s) - 1 and s[k+1] == s[k]:  # skip duplicate char
                k += 1
            i = k + 1
            while k < len(s) - 1 and j > 0 and s[k+1] == s[j-1]:
                k += 1
                j -= 1
            cur_len = k - j + 1
            if cur_len > max_len:
                max_len = cur_len
                start = j
        return s[start: start+max_len]
