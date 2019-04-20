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


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return manacher(s)


def manacher(s):
    # 预处理
    s = '#' + '#'.join(s) + '#'

    RL = [0] * len(s)
    MaxRight = 0
    pos = 0
    MaxLen = 0
    max_pos = 0
    for i in range(len(s)):
        if i < MaxRight:
            RL[i] = min(RL[2 * pos - i], MaxRight - i)
        else:
            RL[i] = 1
        # 尝试扩展，注意处理边界
        while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
            RL[i] += 1
        # 更新MaxRight,pos
        if RL[i] + i - 1 > MaxRight:
            MaxRight = RL[i] + i - 1
            pos = i
        # 更新最长回文串的长度
        if RL[i] > MaxLen:
            MaxLen = RL[i]
            max_pos = i
    # print(MaxLen, max_pos)
    return s[max_pos - (MaxLen-1):max_pos + MaxLen].replace('#', '')


print(Solution2().longestPalindrome('aaaa'))
