# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        n=[]
        while head:
            n.append(head.val)
            head=head.next
        n=sorted(n)
        head=ListNode(-1)
        prev=head
        for i in n:
            prev.next=ListNode(i)
            prev=prev.next
        return head.next