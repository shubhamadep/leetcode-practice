class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0
        def helper(node, maximum):
            if not node:
                return 0
            
            if node.val >= maximum:
                self.count += 1
            
            helper(node.left, max(maximum, node.val))
            helper(node.right, max(maximum, node.val))
        
        helper(root, root.val)
        return self.count