from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return rooms
        
        rows = len(rooms)
        cols = len(rooms[0])
        direc = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        
        
        while queue:
            
            r, c = queue.popleft()
            current_distance = rooms[r][c] + 1
            
            for d in direc:
                
                xr = r + d[0]
                xc = c + d[1]
                
                if 0<= xr <rows and 0 <= xc < cols and rooms[xr][xc] == 2147483647:
                    rooms[xr][xc] = current_distance
                    queue.append((xr,xc))
        
        return rooms