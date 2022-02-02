# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        
        self.sum = 0
        def helper(node):
            if not node:
                return 0
            
            if low <= node.val <= high:
                self.sum += node.val
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.sum
        