class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        prev = root
        
        while queue:
            node = queue.popleft()
            
            if node:
                if not prev:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            
            prev = node
        
        return True