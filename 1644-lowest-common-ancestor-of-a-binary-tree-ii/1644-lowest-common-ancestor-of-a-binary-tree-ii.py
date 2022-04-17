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
                return False
            
            left_node = helper(node.left)
            right_node = helper(node.right)
            curr_node = (node == p or node == q)
            
            if (curr_node and left_node) or (curr_node and right_node) or (left_node and right_node):
                self.lca = node
                return True
            
            return left_node or curr_node or right_node
        
        self.lca = None
        helper(root)
        return self.lca
            
            
            