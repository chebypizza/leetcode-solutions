class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        counter = 0
        n = len(grid)


        def check(row, col, grid):
            grid[row][col] = 0
            if 1 in grid[row]:
                return True
            for i in range(n):
                if grid[i][col] == 1:
                    return True

        for row in range(n):
            for col in range(len(grid[1])):
                if grid[row][col] == 1 and check(row, col, grid):
                    counter += 1
                    grid[row][col] = 1

        return counter