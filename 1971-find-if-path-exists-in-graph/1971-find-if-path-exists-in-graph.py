'''
union find
TC: O(E + VlogV)
Space: O(V)

dfs
TC: O(V + E)
Space: O(V+E)

'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def helper(visited, node, destination):
            if node == destination:
                return True
            
            visited[node] = True
            for neighbor_node in adj_list[node]:
                if not visited[neighbor_node] and helper(visited, neighbor_node, destination):
                    return True
            
            return False
            
        visited = [False] * n
        
        adj_list = collections.defaultdict(list)
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
            
        return helper(visited, source, destination)