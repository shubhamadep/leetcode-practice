class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque()
        zig = True
        q.append(root)
        result = []
        
        while q:
            
            children = []
            while q:
                children.append(q.popleft())
                
            if zig:
                result.append([child.val for child in children])
            else:
                result.append([child.val for child in children[::-1]])

            for child in children:
                
                if child.left:
                    q.append(child.left)
                if child.right:
                    q.append(child.right)
            
            zig = not zig

        return result