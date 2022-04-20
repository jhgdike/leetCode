class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        pre_sum, sum = [0]*n, 0
        left, l = [0] * n, -1
        for i, b in enumerate(s):
            if b == '*':
                sum += 1
            else:
                l = i
            pre_sum[i] = sum
            left[i] = l
        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r
        ans = []
        for query in queries:
            l, r = right[query[0]], left[query[1]]
            if l < 0 or r < 0 or l >= r:
                ans.append(0)
            else:
                ans.append(pre_sum[r]-pre_sum[l])
        return ans

