class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = set()
        
        while p:
            # Record all ancestors of p, including self (p)
            p_ancestors.add(p)
            p = p.parent
            
        while q:
            # if q present in p_ancestors, we found our node (including self (q))
            if q in p_ancestors:
                return q
            q = q.parent
                
        return None