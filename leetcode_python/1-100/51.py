class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        if n in [2, 3]:
            return []
        res = []
        for i in range(n):
            self.find_cur([i], [i], [i], res, n, 1)
        return res

    def find_cur(self, col, plus, cross, res, n, j):
        if j >= n:
            cur_map = [['.'] * n for _ in range(n)]
            for index, y in enumerate(col):
                x = plus[index] - y
                cur_map[x][y] = 'Q'
            res.append([''.join(x) for x in cur_map])
            return
        for k in range(n):
            if (k not in col) and (j + k not in plus) and (k - j) not in cross:
                self.find_cur(col + [k], plus + [j+k], cross + [k-j], res, n, j + 1)


print(Solution().solveNQueens(5))
