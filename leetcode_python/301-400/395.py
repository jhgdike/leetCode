class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 分治法
        if len(s) < k:
            return 0
        for sk in set(s):
            if s.count(sk) < k:
                return max([self.longestSubstring(sl, k) for sl in s.split(sk)])
        return len(s)


s = Solution()
print(s.longestSubstring('aaabb', 3))
print(s.longestSubstring('ababbc', 2))
