# coding: utf-8


class Solution(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        length = len(input)
        for i in range(0, length):
            if input[i] in '+-*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for m in res1:
                    for n in res2:
                        if input[i] == '+':
                            res.append(m + n)
                        elif input[i] == '-':
                            res.append(m - n)
                        else:
                            res.append(m * n)
        if not res:
            res.append(int(input))
        return res

    def diffWaysToCompute_recursion(self, input):
        map_res = {}
        return self._recursion(input, map_res)

    def _recursion(self, input, map_res):
        res = []
        length = len(input)
        for i in range(0, length):
            if input[i] in '+-*':
                left, right = input[:i], input[i+1:]
                if not map_res.get(left):
                    map_res[left] = self._recursion(left, map_res)
                res1 = map_res[left]
                if not map_res.get(right):
                    map_res[right] = self._recursion(right, map_res)
                res2 = map_res[right]
                for m in res1:
                    for n in res2:
                        if input[i] == '+':
                            res.append(m + n)
                        elif input[i] == '-':
                            res.append(m - n)
                        else:
                            res.append(m * n)
        if not res:
            res.append(int(input))
        return res
