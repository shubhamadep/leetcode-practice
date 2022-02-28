class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            self.diameter = max(self.diameter, left + right)
            
            return max(left, right) + 1
        
        helper(root)
        return self.diameter