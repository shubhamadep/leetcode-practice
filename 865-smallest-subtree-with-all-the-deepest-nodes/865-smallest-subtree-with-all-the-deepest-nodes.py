class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        def helper(node):
            if not node:
                return None, 0
            
            left_node, left_depth = helper(node.left)
            right_node, right_depth = helper(node.right)
            
            if left_depth > right_depth:
                return left_node, left_depth + 1
            elif right_depth > left_depth:
                return right_node, right_depth + 1
            else:
                return node, left_depth + 1
        
        node, depth = helper(root)
        return node
        