"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    
        if not head:
            return None
        
        p = head
        while p:
            new_node = Node(p.val, None, None)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next

        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        oldhead = head
        newhead = head.next
        newH = head.next
        
        while oldhead:
            oldhead.next = oldhead.next.next
            newhead.next = newhead.next.next if newhead.next else None
            oldhead = oldhead.next
            newhead = newhead.next
        
        
        return newH
        