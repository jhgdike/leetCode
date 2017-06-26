import collections


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        pattern = 'zabcdefghijklmnopqrstuvwxyz'
        cmap = collections.defaultdict(int)
        start = end = 0
        for c in range(len(p)):
            if c and p[c-1:c+1] not in pattern:
                for x in range(start, end):
                    cmap[p[x]] = max(end - x, cmap[p[x]])
                start = c
            end = c + 1
        for x in range(start, end):
            cmap[p[x]] = max(end - x, cmap[p[x]])
        return sum(cmap.values())
