class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.seen = []
        def buildNumber(node, number):
            if not node:
                return 
            
            number = number*10 + node.val
            if not node.left and not node.right:
                self.seen.append(number)
                return
            buildNumber(node.left, number)
            buildNumber(node.right, number)
        
        buildNumber(root, 0)
        print(self.seen)
        return sum(self.seen)