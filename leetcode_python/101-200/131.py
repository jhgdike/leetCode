class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def dfs(ss, cur):
            if ss == ss[::-1]:
                res.append(cur + [ss])
            for i in range(1, len(ss)):
                if ss[:i] == ss[:i][::-1]:
                    dfs(ss[i:], cur + [ss[:i]])
        dfs(s, [])
        return res


