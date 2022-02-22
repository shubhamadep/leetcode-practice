class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev = None
            while node:
                tempNext = node.next
                node.next = prev
                prev = node
                node = tempNext
            return prev
        
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        head2 = reverse(slow)

        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
            
        return True