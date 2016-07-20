class Solution(object):
    def isValidSudoku(self, board):
        return self.is_valid_row(board) and self.is_valid_col(
            board) and self.is_valid_square(board)

    def is_valid_row(self, board):
        for item in board:
            if not self.is_valid_unit(item):
                return False
        return True

    def is_valid_col(self, board):
        for item in zip(*board):
            if not self.is_valid_unit(item):
                return False
        return True

    def is_valid_square(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                item = [board[x][y] for x in range(i, i + 3) for y in
                        range(j, j + 3)]
                if not self.is_valid_unit(item):
                    return False
        return True

    def is_valid_unit(self, unit):
        nums = [x for x in unit if x != '.']
        return len(set(nums)) == len(nums)
