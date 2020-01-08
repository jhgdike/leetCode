class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n in [2, 3]:
            return 0
        self.res = 0
        for i in range(n):
            self.find_cur([i], [i], [i], n, 1)
        return self.res

    def find_cur(self, col, plus, cross, n, j):
        if j >= n:
            self.res += 1
            return
        for k in range(n):
            if (k not in col) and (j + k not in plus) and (k - j) not in cross:
                self.find_cur(col + [k], plus + [j+k], cross + [k-j], n, j + 1)
