class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.res = False
        if not word:
            return True
        if not board:
            return False
        hold = [[1 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.res:
                    return self.res
                if board[i][j] == word[0]:
                    hold[i][j] = 0
                    self.helper(board, hold, word[1:], i, j)
                    hold[i][j] = 1
        return self.res

    def helper(self, board, hold, word, i, j):
        if self.res:
            return
        if not word:
            self.res = True
            return
        if j + 1 < len(board[0]) and hold[i][j + 1] and board[i][j + 1] == word[0]:
            hold[i][j + 1] = 0
            self.helper(board, hold, word[1:], i, j + 1)
            hold[i][j + 1] = 1
        if j - 1 >= 0 and hold[i][j - 1] and board[i][j - 1] == word[0]:
            hold[i][j - 1] = 0
            self.helper(board, hold, word[1:], i, j - 1)
            hold[i][j - 1] = 1
        if i + 1 < len(board) and hold[i + 1][j] and board[i + 1][j] == word[0]:
            hold[i + 1][j] = 0
            self.helper(board, hold, word[1:], i + 1, j)
            hold[i + 1][j] = 1
        if i - 1 >= 0 and hold[i - 1][j] and board[i - 1][j] == word[0]:
            hold[i - 1][j] = 0
            self.helper(board, hold, word[1:], i - 1, j)
            hold[i - 1][j] = 1

from collections import Counter