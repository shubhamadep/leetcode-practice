class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maximum_diff = float('-inf')
        
        def helper(node, minimum, maximum):
            if not node:
                self.maximum_diff = max(self.maximum_diff, abs(minimum - maximum))
                return
            
            helper(node.left, min(minimum, node.val), max(maximum, node.val))
            helper(node.right, min(minimum, node.val), max(maximum, node.val))
        
        helper(root, root.val, root.val)
        return self.maximum_diff