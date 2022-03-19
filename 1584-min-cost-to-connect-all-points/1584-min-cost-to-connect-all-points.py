class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[x] > self.rank[y]:
                self.root[root_y] = root_x
            elif self.rank[y] > self.rank[x]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_x] += 1
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        union_find = UnionFind(len(points))
        heap = []
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                distance = abs(x2-x1) + abs(y2-y1)
                heap.append([distance, i, j])
        
        heapq.heapify(heap)
        total_edges_required = len(points) - 1
        minimum_cost = 0
        
        while heap and total_edges_required > 0:
            distance, node1, node2 = heapq.heappop(heap)
            if not union_find.is_connected(node1, node2):
                union_find.union(node1, node2)
                minimum_cost += distance
                total_edges_required -= 1
        
        return minimum_cost