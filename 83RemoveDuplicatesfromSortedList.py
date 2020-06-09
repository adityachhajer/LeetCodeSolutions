# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while (cur != None and cur.next != None):
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
