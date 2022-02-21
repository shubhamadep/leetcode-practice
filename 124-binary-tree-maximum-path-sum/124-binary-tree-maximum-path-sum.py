'''

sum from left, right 
possible answers:
    (node.val + left + right)
    
    return (node.val + left, node.val + right)

'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):            
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maximum_path_until = max(left+node.val, right+node.val, node.val)
            self.maximum = max(self.maximum, maximum_path_until, left+right+node.val)
            
            return maximum_path_until
            
        self.maximum = float('-inf')
        dfs(root)
        return self.maximum
        