class Codec:

    def serialize(self, root):
        
        if not root:
            return 'X'
        
        leftTree = self.serialize(root.left)
        rightTree = self.serialize(root.right)
        
        return str(root.val) + ',' + leftTree + ',' + rightTree
        

    def deserialize(self, data):
        
        self.q = collections.deque(data.split(','))
        
        def helper():
            if not self.q:
                return None
            
            val = self.q.popleft()
            if val == 'X':
                return None
            
            node = TreeNode(val)

            node.left = helper()
            node.right = helper()
            
            return node
            
        return helper()