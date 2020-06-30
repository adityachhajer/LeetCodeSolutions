# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1,n2=0,0
        while l1:
            n1*=10
            n1+=l1.val
            l1=l1.next
        while l2:
            n2*=10
            n2+=l2.val
            l2=l2.next
        n3=n1+n2
        prev=ListNode(-1)
        head=prev
        for i in str(n3):
            head.next=ListNode(i)
            head=head.next
        return prev.next