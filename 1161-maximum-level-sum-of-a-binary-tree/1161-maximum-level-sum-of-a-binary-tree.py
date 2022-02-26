class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        max_sum = float('-inf')
        max_level = 1
        current_level = 1
        
        while queue:
            
            children = []
            while queue:
                children.append(queue.popleft())
                
            temp_sum = 0
            for child in children:
                temp_sum += child.val
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
            
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_level = current_level
        
            current_level += 1
            
        return max_level