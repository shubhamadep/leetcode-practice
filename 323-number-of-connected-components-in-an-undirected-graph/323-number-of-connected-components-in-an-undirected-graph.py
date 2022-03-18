class UnionFind:
    def __init__(self, n):
        self.roots = [x for x in range(n)]
        self.ranks = [1] * n
        self.counts = n
        
    def find(self, node):
        if self.roots[node] == node:
            return node
        self.roots[node] = self.find(self.roots[node])
        return self.roots[node]
    
    def union(self, node1, node2):
        node1_root = self.find(node1)
        node2_root = self.find(node2)
        
        if node1_root != node2_root:
            if self.ranks[node1_root] > self.ranks[node2_root]:
                self.roots[node2_root] = node1_root
            elif self.ranks[node1_root] < self.ranks[node2_root]:
                self.roots[node1_root] = node2_root
            else:
                self.roots[node1_root] = node2_root
                self.ranks[node1_root] += 1
            self.counts -= 1
            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for edge in edges:
            union_find.union(edge[0], edge[1])
        
        return union_find.counts