class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        left_boundary = [root.val]
        leaves = []
        right_boundary = []
        if root.left:
            n = root.left
            while n.left or n.right:
                left_boundary.append(n.val)
                if n.left:
                    n = n.left
                else:
                    n = n.right
        if root.right:
            n = root.right
            while n.right or n.left:
                right_boundary.append(n.val)
                if n.right:
                    n = n.right
                else:
                    n = n.left
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return left_boundary + leaves + right_boundary[::-1]