class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ans = 0
        div = dict()
        for i in range(len(equations)):
            div[equations[i][0]].setdefault([]).append((equations[i][1], values[i]))
            div[equations[i][1]].setdefault([]).append((equations[i][0], 1.0/values[i]))
        ans = [-1.0] * len(queries)
        for i, query in enumerate(queries):
            if query[0] not in div or query[1] not in div:
                continue
            
            ans[i] = 0
