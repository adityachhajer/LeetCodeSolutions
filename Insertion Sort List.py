# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        l.sort()
        head = ListNode(l.pop(0))
        cur = head
        while l:
            cur.next = ListNode(l.pop(0))
            cur = cur.next
        return head
