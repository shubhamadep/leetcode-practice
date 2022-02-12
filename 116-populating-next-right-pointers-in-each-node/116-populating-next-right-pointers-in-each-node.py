class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            while head:
                
                #connection 1
                head.left.next = head.right
                
                #connection 2
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            
            leftmost = leftmost.left
        
        return root
        