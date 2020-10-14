# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        a.sort()
        da = ListNode(1)
        head = da
        while a:
            head.next = ListNode(a.pop(0))
            head = head.next
        return da.next
