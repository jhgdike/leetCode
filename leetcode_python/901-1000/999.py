class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        m, n = self.find_r(board)
        for i in range(m - 1, -1, -1):
            if board[i][n] == 'B':
                break
            if board[i][n] == 'p':
                res += 1
                break
        for i in range(m + 1, len(board)):
            if board[i][n] == 'B':
                break
            if board[i][n] == 'p':
                res += 1
                break
        for i in range(n - 1, -1, -1):
            if board[m][i] == 'B':
                break
            if board[m][i] == 'p':
                res += 1
                break
        for i in range(n + 1, len(board[0])):
            if board[m][i] == 'B':
                break
            if board[m][i] == 'p':
                res += 1
                break
        return res

    def find_r(self, board):
        m = n = 0
        while m < len(board):
            n = 0
            while n < len(board[0]):
                if board[m][n] == 'R':
                    return m, n
                n += 1
            m += 1


board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]


print(Solution().find_r(board))
