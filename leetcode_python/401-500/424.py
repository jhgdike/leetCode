class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) <= k - 1:
            return len(s)
        nums = [0] * 26
        n = len(s)
        max_ = l = r = 0
        while r < n:
            nums[ord(s[r])-ord('A')] += 1
            max_ = max(max_, nums[ord(s[r])-ord('A')])
            if r - l + 1 - max_ > k:
                nums[ord(s[l])-ord('A')] -= 1
                l += 1
            r += 1
        return r - l


print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("AABABBA", 1))
