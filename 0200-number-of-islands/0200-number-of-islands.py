class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def check(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != '1':
                return
            else:
                grid[row][col] = '0'
                check(row + 1, col)
                check(row - 1, col)
                check(row, col + 1)
                check(row, col - 1)

        res = 0
        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == '1'):
                    res += 1
                    check(row, col)

        return res