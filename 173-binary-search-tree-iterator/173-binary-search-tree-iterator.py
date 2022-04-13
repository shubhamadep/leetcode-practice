# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [] 
        self.root = root
        self.addLeftchildren(root)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.addLeftchildren(node.right)
        return node.val
    
    def addLeftchildren(self, node):
        self.stack.append(node)
        while node.left:
            self.stack.append(node.left)
            node = node.left

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
