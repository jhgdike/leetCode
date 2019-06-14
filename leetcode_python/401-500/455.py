class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        sj = 0
        for i in g:
            while sj < len(s) and s[sj] < i:
                sj += 1
            if sj >= len(s):
                break
            count += 1
            sj += 1
        return count


print(Solution().findContentChildren([1,2], [1,2,3]))
