class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return []
        
        def helper(node):
            if not node:
                return None
            
            if not node.left and not node.right:
                return node
            
            left = helper(node.left)
            right = helper(node.right)
            
            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            
            return right if right else left
        
        return helper(root)
        
        