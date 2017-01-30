class Solution(object):

    def generateMatrix(self, n):
        if not n:
            return []
        res = [[0 for i in range(n)] for j in range(n)]
        inc = 1
        i = j = 0
        while True:
            while j < n and res[i][j] == 0:
                res[i][j] = inc
                inc += 1
                j += 1
            j -= 1
            i += 1
            while i < n and res[i][j] == 0:
                res[i][j] = inc
                inc += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and res[i][j] == 0:
                res[i][j] = inc
                inc += 1
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and res[i][j] == 0:
                res[i][j] = inc
                inc += 1
                i -= 1
            i += 1
            j += 1
            if inc > n * n:
                break
        return res
