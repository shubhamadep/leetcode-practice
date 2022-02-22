class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def check_boundary(x, y):
            return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))
        
        def dfs(r, c):
            directions = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            max_area = 1
            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if check_boundary(nr, nc) and grid[nr][nc] == 1:
                    max_area += dfs(nr, nc)
            
            return max_area
        
        self.ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.ans = max(self.ans, dfs(row, col))
        
        return self.ans