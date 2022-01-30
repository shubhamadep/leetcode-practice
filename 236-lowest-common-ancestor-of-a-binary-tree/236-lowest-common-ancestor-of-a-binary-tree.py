class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLCA(node):
            if not node:
                return 0
            
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            mid = (node == p) or (node == q)
            
            if (left and mid) or (right and mid) or (left and right):
                self.commonAncestor = node
            
            return left or mid or right
        
        self.commonAncestor = 0
        findLCA(root)
        
        return self.commonAncestor