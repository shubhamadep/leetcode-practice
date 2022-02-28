class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []
        
        while queue:
            children = []
            while queue:
                children.append(queue.popleft())
            
            for child in children:
                if child.left:
                    queue.append(child.left)
                
                if child.right:
                    queue.append(child.right)
            
            result.append(child.val)
        
        return result
            
        