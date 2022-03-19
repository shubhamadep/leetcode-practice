class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start, end = 0, len(graph)-1
        memo = {}
        
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            
            if idx == end:
                return [[end]]
            
            result = []
            for neighbor in graph[idx]:
                for path in dfs(neighbor):
                    result.append([idx]+path)
            
            memo[idx] = result
            return result
        
        return dfs(0)
            
        