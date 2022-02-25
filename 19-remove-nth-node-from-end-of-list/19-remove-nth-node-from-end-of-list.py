class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        first, second = dummy, dummy
        for i in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
    
        second.next = second.next.next
        
        return dummy.next