class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dic = [-1] * 255
        max_l = j = -1
        for i, x in enumerate(s):
            j = max(j, dic[ord(x)])
            max_l = max(max_l, i - j)
            dic[ord(x)] = i
        return max_l
