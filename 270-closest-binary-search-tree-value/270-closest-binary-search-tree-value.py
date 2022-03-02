class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def helper(node):
            if not node:
                return 
            
            diff = abs(node.val - target)
            if diff < self.min_diff:
                self.min_diff = diff
                self.result = node.val
            
            if target > node.val:
                helper(node.right)
            else:
                helper(node.left)
        
        self.min_diff = float('inf')
        self.result = root.val
        
        helper(root)
        
        return self.result