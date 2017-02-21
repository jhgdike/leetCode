class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.trans_2_py(board)
        self.solve(board, 0)
        self.trans_2_str(board)

    def trans_2_py(self, board):
        for i in range(len(board)):
            board[i] = [int(x) if x != '.' else 0 for x in board[i]]

    def trans_2_str(self, board):
        for i in range(len(board)):
            board[i] = ''.join([str(x) for x in board[i]])

    def check(self, board, row, col, num):
        for i in range(9):
            x = row / 3 * 3 + i / 3
            y = col / 3 * 3 + i % 3
            if board[i][col] == num or board[row][i] == num or board[x][y] == num:
                return False
        return True

    def solve(self, board, position):
        if position >= 81:
            return True
        row = position / 9
        col = position % 9
        if board[row][col] == 0:
            for i in range(1, 10):
                if self.check(board, row, col, i):
                    board[row][col] = i
                    if self.solve(board, position + 1):
                        return True
                board[row][col] = 0
        else:
            return self.solve(board, position + 1)
