class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True] + [False] * len(s)
        for i in range(len(s)+1):
            if dp[i]:
                for word in wordDict:
                    if word == s[i:i+len(word)]:
                        dp[i+len(word)] = True
        return dp[-1]
