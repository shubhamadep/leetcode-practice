class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        seen = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        directions = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
        ans = 0
        
        while heap:
            value, row, col = heapq.heappop(heap)
            ans = max(ans, value)
            if row == col == len(grid)-1:
                return ans
            for direction in directions:
                new_row, new_col = row+direction[0], col + direction[1]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in seen:
                    heapq.heappush(heap, (grid[new_row][new_col], new_row, new_col))
                    seen.add((new_row, new_col))