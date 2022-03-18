class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(v):
            for neighbor_index, neighbor in enumerate(isConnected[v]):
                if neighbor == 1 and neighbor_index not in visited:
                    visited.add(neighbor_index)
                    dfs(neighbor_index)
        
        visited = set()
        group = 0
        for vertex in range(len(isConnected)):
            if vertex not in visited:
                dfs(vertex)
                group += 1
        
        return group