class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1

            head = node = ListNode(-1, None)
            while l1 and l2:
                num1, num2 = l1.val, l2.val
                if num1 <= num2:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next

            if l1:
                node.next = l1
            if l2:
                node.next = l2
        
            return head.next
        
        numberofLists = len(lists)
        interval = 1
        
        while interval < numberofLists:
            i = 0
            for i in range(0, numberofLists-interval, interval*2):
                lists[i] = merge(lists[i], lists[i+interval])
            interval *= 2
        
        return lists[0] if numberofLists > 0 else None