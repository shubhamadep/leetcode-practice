class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[+1, 0], [-1, 0], [0, +1], [0, -1]]
        islands = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1            
                    queue = collections.deque()
                    queue.append((row, col))
                    
                    while queue:
                        r, c = queue.pop()
                        for direction in directions:
                            new_row, new_col = r+direction[0], c+direction[1]
                            if len(grid) > new_row >= 0 and len(grid[0]) > new_col >= 0 and grid[new_row][new_col]=="1":
                                queue.append((new_row, new_col))
                        grid[r][c] = 0
        
        return islands