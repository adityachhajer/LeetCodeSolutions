class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        a = head
        a_nxt = head.next
        # create a stack with the nodes
        stack = []
        while head:
            stack.append(head)
            head = head.next
        b = stack.pop() # b pointer is the last node
        b_prev = None   # b_prev is the node before the last
        while a != b_prev and b != a_nxt:
            b_prev = stack.pop()
            a.next = b
            b.next = a_nxt
            b_prev.next = None
            # update a, b and a_nxt pointers
            a = a_nxt
            b = b_prev
            a_nxt = a.next