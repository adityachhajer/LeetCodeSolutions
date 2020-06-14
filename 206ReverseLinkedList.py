# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        l = []
        while head:
            l.append(head)
            head = head.next
        head = l.pop()
        cur = head
        while (len(l) != 0):
            cur.next = l.pop()
            cur = cur.next
        cur.next = None
        return head
