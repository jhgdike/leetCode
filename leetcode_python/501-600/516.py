class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


class Solution2(object):
    """求的是最长子序列，而不是最长子串，不可以用这种方法"""
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]: j += 1
            l, r = i - 1, j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            res = max(res, r - l - 1)
            i = j
        return res


# 马拉车求最长回文子串
def manacher(s):
    #预处理
    s='#'+'#'.join(s)+'#'

    RL=[0]*len(s)
    MaxRight=0
    pos=0
    MaxLen=0
    for i in range(len(s)):
        if i<MaxRight:
            RL[i]=min(RL[2*pos-i], MaxRight-i)
        else:
            RL[i]=1
        #尝试扩展，注意处理边界
        while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
            RL[i]+=1
        #更新MaxRight,pos
        if RL[i]+i-1>MaxRight:
            MaxRight=RL[i]+i-1
            pos=i
        #更新最长回文串的长度
        MaxLen=max(MaxLen, RL[i])
    return MaxLen-1
