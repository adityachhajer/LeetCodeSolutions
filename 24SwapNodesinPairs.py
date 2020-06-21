class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:return
        prev,nxt=head,head.next
        while nxt:
            prev.val,nxt.val=nxt.val,prev.val
            if nxt.next:
                prev=prev.next.next
                nxt=nxt.next.next
            else:break
        return head