class Solution:
    def __init__(self):
        self.visited = defaultdict()
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val, [])
        self.visited[node] = new_node
        
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))
        
        return new_node
        