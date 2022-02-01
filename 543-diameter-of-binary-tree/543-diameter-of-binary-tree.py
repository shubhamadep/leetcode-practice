class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.maxd = 0
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            self.maxd = max(self.maxd, left + right)
            
            return max(left, right) + 1
        
        helper(root)
        return self.maxd