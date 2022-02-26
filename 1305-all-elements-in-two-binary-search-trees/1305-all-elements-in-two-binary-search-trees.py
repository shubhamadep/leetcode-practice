class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def in_order(node):
            if not node:
                return None
            
            in_order(node.left)
            self.temp.append(node.val)
            in_order(node.right)
        
        
        self.temp = []
        in_order(root1)
        tree1 = self.temp
        
        self.temp = []
        in_order(root2)
        tree2 = self.temp
        
        i, j = 0, 0
        result = []
        while i < len(tree1) and j < len(tree2):
            if tree1[i] < tree2[j]:
                result.append(tree1[i])
                i += 1
            else:
                result.append(tree2[j])
                j += 1
        
        while j < len(tree2):
            result.append(tree2[j])
            j += 1
        
        while i < len(tree1):
            result.append(tree1[i])
            i += 1
        
        return result