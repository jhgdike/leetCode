import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        alph = collections.defaultdict(int)
        p_counts = collections.Counter(p)
        p_diff = len(p_counts.keys())
        equal = l = r = 0
        ans = []
        while r < len(s):
            cur = s[r]
            if cur not in p_counts:
                alph.clear()
                equal = 0
                l = r = r + 1
            else:
                alph[cur] += 1
                if alph[cur] == p_counts[cur]:
                    equal += 1
                if r - l + 1 == len(p):
                    if equal == p_diff:
                        ans.append(l)
                    if alph[s[l]] == p_counts[s[l]]:
                        equal -= 1
                    alph[s[l]] -= 1
                    l += 1
                r += 1
        return ans


sl = Solution()
print(sl.findAnagrams('cbaebabacd', 'abc'))
