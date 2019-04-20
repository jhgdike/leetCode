"""
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

技术：滑动窗口+计数索引（不知道是不是这样叫，可以理解为简单的Hash表实现）
这道题有一定难度，leetcode438 号题也可使用类似的思路，不过稍微简单一些。

1. 注意到题目的关键："所有字母的最小子串"，也就是说两个串都只能是字母。
2. 于是，可以开辟一个大小为64的数组，来存放数组中字母的频率(Frequency)。准确的说，
   通过字母的ASCII码作为数组的索引，开辟空间的大小为26+6+26=58：26个大写字母，26个小写字母，
   还有中间的6个非字母  A~Z[65~90]  非字母[91~96]  a~z[97~122]
3. 滑动窗口的使用：分三种情况来移动窗口：（这里令当前窗口的左右边界分别为l，r，窗口的大小为winSize=r-l+1）
   1) 当winSize < t.size()  r++;  也就是窗口右边界向右移动
   2) 当winSize == t.size() :
       2.1) 当窗口中的字符已经符合要求了，直接返回return，已经找到了
       2.2) 否则r++，窗口右边界向右移动
   3) 当winSize > t.size()
       2.1) 当窗口中的字符已经符合要求了，l++，窗口左边界向右移动
       2.2) 否则r++，窗口右边界向右移动

4. 上面是滑动窗口的使用思路，具体实现上有一定的不同，下面是需要考虑到的要点：
   1) 啥叫作窗口中的字符已经符合要求了？
   1) 窗口滑动时的操作是关键
   2) 要考虑到数组越界的问题

"""
from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        s_freq = [0] * 64
        t_freq = Counter(t)
        l, r = 0, -1
        edge = [-1, len(s) + 1]
        while l <= len(s) - len(t):
            # 直接窗口右边界右移，循环continue
            if r - l + 1 < len(t):
                if r + 1 < len(s):
                    r += 1
                    s_freq[ord(s[r]) - 65] += 1
                    continue
                break
            flag = True
            for k, v in t_freq.items():
                if s_freq[ord(k) - 65] < v:
                    flag = False
                    while r + 1 < len(s):
                        r += 1
                        s_freq[ord(s[r]) - 65] += 1
                        if s_freq[ord(k) - 65] >= v:
                            flag = True
                            break
            if not flag:
                break

            if r - l + 1 == len(t):
                return s[l:r + 1]
            else:
                if r - l < edge[1] - edge[0]:
                    edge = [l, r]
                s_freq[ord(s[l]) - 65] -= 1
                l += 1
        return '' if edge[0] == -1 else s[edge[0]:edge[1] + 1]


print(Solution().minWindow('ADOBECODEBANC', 'ABC'))


class Solution2(object):
    def minWindow(self, s, t):
        """
        """

        if len(t) > len(s):
            return ""
        max_length = len(s)
        tmp_max = max_length + 1
        left = 0
        right = 0
        count = 0
        str_dict = {}
        for char in t:
            if char in str_dict:
                str_dict[char] += 1
            else:
                str_dict[char] = 1

        result = ""
        while (right < max_length):
            if s[right] in str_dict:
                str_dict[s[right]] -= 1
                if str_dict[s[right]] >= 0:
                    count += 1

            while (count == len(t)):
                if (right - left + 1) < tmp_max:
                    tmp_max = right - left + 1
                    result = s[left: right + 1]
                if s[left] in str_dict:
                    str_dict[s[left]] += 1
                    if str_dict[s[left]] >= 1:
                        count -= 1
                left += 1
            right += 1

        return result
