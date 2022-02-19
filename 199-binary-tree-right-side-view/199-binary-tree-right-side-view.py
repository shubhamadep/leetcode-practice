class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        queue = collections.deque()
        queue.append(root)
        while queue:
            tempQueue = queue
            queue = collections.deque()
            while tempQueue:
                node = tempQueue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(node.val)
        
        return ans