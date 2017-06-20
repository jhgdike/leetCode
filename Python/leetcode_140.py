class Solution(object):

    """难度较高，先不做了"""
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [[-1]] + [[] for _ in range(len(s))]
        for i in range(len(s)):
            if dp[i]:
                for item in wordDict:
                    if item == s[i:i+len(item)]:
                        dp[i+len(item)].append(i)

