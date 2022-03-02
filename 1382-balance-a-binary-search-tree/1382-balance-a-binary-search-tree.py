# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            self.order.append(node.val)
            dfs(node.right)
        
        def build_bst(start, end, order):
            if start > end:
                return
            
            mid = end + (start - end) // 2
            node = TreeNode(order[mid], None, None)
            node.left = build_bst(start, mid-1, order)
            node.right = build_bst(mid+1, end, order)
            
            return node
        
        self.order = []
        dfs(root)
        return build_bst(0, len(self.order)-1, self.order)