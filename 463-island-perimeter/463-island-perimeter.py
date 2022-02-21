class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        directions = ((+1, 0), (-1, 0), (0, +1), (0, -1))
        
        def isBound(r, c):
            return (0 <= r < len(grid)) and (0 <= c < len(grid[0]))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    for direction in directions:
                        nr, nc = row+direction[0], col+direction[1]
                        bound = isBound(nr, nc)
                        if not bound:
                            perimeter += 1
                        elif bound and grid[nr][nc] == 0:
                            perimeter += 1
        
        return perimeter
        