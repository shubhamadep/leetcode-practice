# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/discuss/1039022/Python-DFS-O(N)-Explained-%22Similar-to-All-Nodes-Distance-K-in-Binary-Tree%22

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.closestLeaf = [float("inf"), root.val]
        
        # Returns distance from the target node if found else returns None.
        def findTarget(node, target):
            if not node:
                return None
            
            if node.val == target:
                # find all leaves under the target node
                findClosestLeafBelow(node, 0)
                return 0
            
            # Look for the closest leaf in the opposite branch where the target node was found
            L, R = findTarget(node.left, target), findTarget(node.right, target)
            if L != None:
                findClosestLeafBelow(node.right, L+2)
                return L+1
            if R != None:
                findClosestLeafBelow(node.left, R+2)
                return R+1
            
            return None 
        
        def findClosestLeafBelow(node, distance):
            if not node:
                return
            
            # If we are already further than closest leaf found so far no point searching further
            if distance > self.closestLeaf[0]:
                return
        
            if node.left:
                findClosestLeafBelow(node.left, distance + 1)
            if node.right:
                findClosestLeafBelow(node.right, distance + 1)
            if not node.left and not node.right and distance < self.closestLeaf[0]:
                self.closestLeaf = [distance, node.val]
        
        targetDepth = findTarget(root, k)
        
        return self.closestLeaf[1]