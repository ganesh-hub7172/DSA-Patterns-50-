class Solution:
    def removeNodes(self, head):
        
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        head = reverse(head)
        
        max_val = head.val
        curr = head
        
        while curr and curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val
        
        return reverse(head)