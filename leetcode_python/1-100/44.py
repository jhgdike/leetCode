class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count('*') > len(s):
            return False
        dp = [True] + [False] * len(s)
        for i in p:
            if i != '*':
                for n in reversed(range(len(s))):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, len(s) + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]


class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_cur, p_cur, s_star, p_star = 0, 0, -1, -1
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1
            elif p_cur < len(p) and p[p_cur] == '*':
                p_star = p_cur
                s_star = s_cur
                p_cur += 1
            elif p_star != -1:
                s_star += 1
                p_cur = p_star + 1
                s_cur = s_star
            else:
                return False
        while p_cur < len(p) and p[p_cur] == '*':
            p_cur += 1
        return p_cur == len(p)

ss = [('aa', 'a'), ('aa', '*'), ('cb', '?a'), ('adceb', '*a*b'), ('acdcb', 'a*c?b')]