import collections, numpy

class Solution:
    def __init__(self):
        self.EMPTY, self.BUILDING, self.OBSTACLE = 0, 1, 2
        
    def bfs(self, startingBuildingPos, buildingsVisitedSoFar, grid, gridSumDists):
        
        curX, curY = startingBuildingPos
        queue = collections.deque([((curX+1, curY), 1), ((curX-1, curY), 1), ((curX, curY-1), 1), ((curX, curY+1), 1)])

        while len(queue) != 0:
            
            (curX, curY), steps = queue.popleft()
            if curX < 0 or curX >= len(grid) or curY < 0 or curY >= len(grid[0]):
                continue
            
            # if land was not visited by all building so far or was already visited this round
            if grid[curX][curY] != -buildingsVisitedSoFar:
                continue
            
            gridSumDists[curX][curY] += steps
            grid[curX][curY] -= 1
            
            for nextPos in [(curX+1, curY), (curX-1, curY), (curX, curY-1), (curX, curY+1)]:
                queue.append((nextPos, steps+1))
        
              
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        gridSumDists = numpy.array([[0]*len(grid[0])]*len(grid))
        
        # for each building, sum distance to each empty land
        buildingsVisitedSoFar = 0
        for curX in range(len(grid)):
            for curY in range(len(grid[0])):
                if grid[curX][curY] == self.BUILDING:
                    self.bfs((curX, curY), buildingsVisitedSoFar, grid, gridSumDists)        
                    buildingsVisitedSoFar += 1
           
        # find land with minimum distance sum
        minDistance = 2**31
        for curX in range(len(grid)):
            for curY in range(len(grid[0])):       
                if (grid[curX][curY] == -buildingsVisitedSoFar):
                    minDistance = min(minDistance, gridSumDists[curX][curY])
        if minDistance == 2**31:
            return -1
        
        return minDistance