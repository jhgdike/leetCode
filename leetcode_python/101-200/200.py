class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    filter_island(grid, i, j)
        return count


def filter_island(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return

    grid[i][j] = '0'
    filter_island(grid, i, j+1)
    filter_island(grid, i, j - 1)
    filter_island(grid, i+1, j)
    filter_island(grid, i - 1, j)
