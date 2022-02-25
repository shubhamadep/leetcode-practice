class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque([root])
        zig = True
        result = []
        
        while q:
            children = []
            while q:
                children.append(q.popleft())
                
            if zig:
                result.append([x.val for x in children])
            else:
                result.append([x.val for x in children[::-1]])
            
            for node in children:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            zig = not zig
                  
        return result
            