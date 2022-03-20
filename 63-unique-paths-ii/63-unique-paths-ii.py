class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        
        grid[0][0] = 1 #1 path to reach the start
        
        for i in range(1, rows):
            grid[i][0] = int(grid[i][0] == 0 and grid[i-1][0] == 1)
        
        for j in range(1, columns):
            grid[0][j] = int(grid[0][j] == 0 and grid[0][j-1] == 1)
        
        for i in range(1, rows):
            for j in range(1, columns):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 0

        return grid[rows-1][columns-1]
    