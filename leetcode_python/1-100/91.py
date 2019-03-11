"""
Decode Ways
********
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        n = len(s)
        if n == 1: return 1
        f_1, f_2 = 1, 1
        for i in range(1, n):
            tmp = f_1
            a, b = self.is_valid(s[i]), self.is_valid(s[i-1], s[i])
            if a and b: f_1 += f_2
            elif not a and b: f_1 = f_2
            elif not a and not b: return 0
            f_2 = tmp

        return f_1

    def is_valid(self, a, b=None):
        if b:
            return a == '1' or (a == '2' and b <= '6')
        return a != '0'
