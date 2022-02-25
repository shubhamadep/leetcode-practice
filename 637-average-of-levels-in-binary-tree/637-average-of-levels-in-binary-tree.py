class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        q = collections.deque([root])
        result = []
        
        while q:
            children = []
            while q:
                children.append(q.pop())
            result.append(sum([x.val for x in children]) / len(children))
            
            for node in children:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return result
        