# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=''
        b=''
        while l1 and l2:
            a=a+str(l1.val)
            b=b+str(l2.val)
            l1=l1.next
            l2=l2.next
        while l1:
            a=a+str(l1.val)
            l1=l1.next
        while l2:
            b=b+str(l2.val)
            l2=l2.next
        x=str(int(a)+int(b))
        d=ListNode(0)
        head=d
        for i in range(len(x)):
            head.next=ListNode(int(x[i]))
            head=head.next
        return d.next