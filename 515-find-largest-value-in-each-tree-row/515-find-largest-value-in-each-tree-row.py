class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        result = []
        
        while queue:
            children = []
            max_child = float('-inf')
            while queue:
                node = queue.popleft()
                max_child = max(max_child, node.val)
                children.append(node)
            
            result.append(max_child)
            for node in children:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
            
        