# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        x=[]
        while head:
            if head.val !=val :
                x.append(head.val)
            head=head.next
        head=ListNode(-1)
        prev=head
        for i in x:
            prev.next=ListNode(i)
            prev=prev.next
        return head.next