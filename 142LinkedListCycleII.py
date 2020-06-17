# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        l = []
        while head:
            if head not in l:
                l.append(head)
                head = head.next
            else:
                return head
        return None
