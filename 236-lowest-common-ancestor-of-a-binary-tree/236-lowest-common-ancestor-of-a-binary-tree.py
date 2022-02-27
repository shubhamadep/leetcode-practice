# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if not node:
                return None
            
            mid = node == p or node == q
            
            left = helper(node.left)
            right = helper(node.right)
            
            if (left and mid) or (right and mid) or (left and right):
                return node
            
            return left or right or mid
        
        return helper(root)
            
            
            