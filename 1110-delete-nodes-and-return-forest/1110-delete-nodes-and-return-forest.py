class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:     
        self.to_delete = set(to_delete)
        self.result = []
        
        root = self.dfs(root)
        if root.val not in self.to_delete:
            self.result.append(root)
        return self.result
    
    def dfs(self, root):
        if not root:
            return
        
        root.left = self.dfs(root.left)
        root.right = self.dfs(root.right)
        
        if root.left and root.left.val in self.to_delete:
            self.to_delete.remove(root.left.val)
            root.left = None
            
        if root.right and root.right.val in self.to_delete:
            self.to_delete.remove(root.right.val)
            root.right = None
        
        if root.val in self.to_delete:
            if root.left: 
                self.result.append(root.left)
                root.left = None
            if root.right: 
                self.result.append(root.right)
                root.right = None
        return root