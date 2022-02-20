class Solution:
    def bst(self, nums, i, j):
        if i > j:
            return None
        mid = (i+j) // 2
        node = TreeNode(nums[mid])
        node.left = self.bst(nums, i, mid-1)
        node.right = self.bst(nums, mid+1, j)
        return node
    
    def dfs(self, node):
        if not node:
            return None
        
        self.dfs(node.left)
        self.order.append(node.val)
        self.dfs(node.right)
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.order = []
        self.dfs(root)
        return self.bst(self.order, 0, len(self.order)-1)
            
            