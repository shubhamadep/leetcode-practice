class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def findDepth(node):
            depth = 0
            while node.parent:
                node = node.parent
                depth += 1
            return depth
        
        pd = findDepth(p)
        qd = findDepth(q)
        
        if pd > qd:
            while pd != qd:
                p = p.parent
                pd -= 1
        elif qd > pd:
            while pd != qd:
                q = q.parent
                qd -= 1
        
        while p.val != q.val:
            p = p.parent
            q = q.parent
        
        return p
        
            
            
        
            
            