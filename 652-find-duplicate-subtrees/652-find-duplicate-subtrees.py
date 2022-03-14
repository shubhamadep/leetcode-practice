class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return []
        self.result = []
        self.duplicate_count = defaultdict(int)
        
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        
        if not root:
            return
        left_side = self.dfs(root.left)
        right_side = self.dfs(root.right)
        
        pattern = tuple([left_side, root.val,right_side])
        if pattern in self.duplicate_count and self.duplicate_count[pattern] == 1:
            self.result.append(root)
        self.duplicate_count[pattern] += 1
        
        return pattern