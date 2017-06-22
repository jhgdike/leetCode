class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row, col = len(dungeon), len(dungeon[0])
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i == row - 1 and j == col - 1:
                    dungeon[i][j] = max(1, 1-dungeon[i][j])
                elif i == row - 1:
                    dungeon[i][j] = max(1, dungeon[i][j+1] - dungeon[i][j])
                elif j == col - 1:
                    dungeon[i][j] = max(1, dungeon[i+1][j] - dungeon[i][j])
                else:
                    dungeon[i][j] = max(1, min(dungeon[i+1][j], dungeon[i][j+1]) - dungeon[i][j])

        return dungeon[0][0]
