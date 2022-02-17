class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        queue = deque()
        queue.append((root,0))
        columnmap = defaultdict(list)
        
        result = []
        
        while queue:
            
            curr, col = queue.popleft()
            
            
            if curr:
                columnmap[col].append(curr.val)
                
                queue.append((curr.left, col - 1))
                queue.append((curr.right, col + 1))
        
        
        for i in sorted(columnmap.keys()):
            
            result.append(columnmap[i])
        
        return result