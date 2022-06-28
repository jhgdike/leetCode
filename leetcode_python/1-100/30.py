class Solution1(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or words == []:
            return []
        lenstr = len(s)
        lenword = len(words[0])
        lensubstr = len(words) * lenword
        times = {}
        for word in words:
            if word in times:
                times[word] += 1
            else:
                times[word] = 1
        ans = []
        for i in range(min(lenword, lenstr - lensubstr + 1)):
            self.findAnswer(i, lenstr, lenword, lensubstr, s, times, ans)
        return ans

    def findAnswer(self, strstart, lenstr, lenword, lensubstr, s, times, ans):
        wordstart = strstart
        curr = {}
        while strstart + lensubstr <= lenstr:
            word = s[wordstart:wordstart + lenword]
            wordstart += lenword
            if word not in times:
                strstart = wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word] += 1
                else:
                    curr[word] = 1
                while curr[word] > times[word]:
                    curr[s[strstart:strstart + lenword]] -= 1
                    strstart += lenword
                if wordstart - strstart == lensubstr:
                    ans.append(strstart)


import collections


# 滑动窗口加缓存
# 整体思路，滑动窗口大小无疑是n*m，如果是简单的滑动窗口，则无法有效利用之前的缓存结果，所以可以分批滑动，总共滑动n次，每次滑动跳n个格子
# 123 123 123 123、 1 231 231 231 23、 12 312 312 312 3
# 如上，每个单次长度为3，则可以滑动三次，一次移动n个单位
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m, n, ls = len(words), len(words[0]), len(s)
        base = collections.Counter(words)
        ans = []
        for i in range(n):
            if m * n + i > ls:
                break
            sc = base.copy()
            for j in range(m):
                sc[s[j * n + i:(j + 1) * n + i]] -= 1
            start = i
            while start <= ls - n * m:
                if max(sc.values()) == 0:
                    ans.append(start)
                sc[s[start:start + n]] += 1
                sc[s[start+n*m:start+(m+1)*n]] -= 1
                start += n
        return ans


print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
