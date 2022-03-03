class Solution:
    def diameter(self, root: 'Node') -> int:
        self.diameter = float('-inf')
        
        def helper(node):
            if not node:
                return 0
            
            max_1, max_2 = 0, 0
            for child in node.children:
                depth = helper(child) + 1
                if depth > max_1:
                    max_1, max_2 = depth, max_1
                elif depth > max_2:
                    max_2 = depth
            
            self.diameter = max(max_1+max_2, self.diameter)
            return max(max_1, max_2)
        
        helper(root)
        return self.diameter