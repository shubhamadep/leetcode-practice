class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Dynamic programming - storing min to reach a point from   destination.
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                #elements on the bottom of the row
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    grid[i][j] += grid[i][j+1]
                #elements on the right column
                if j == len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] += grid[i+1][j]
                #elements not on the border.
                if j != len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]