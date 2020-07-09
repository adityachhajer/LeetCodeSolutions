# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        di={}
        while head:
            if head.val not in di.keys():
                di[head.val]=1
            else:
                di[head.val]+=1
            head=head.next
        head=ListNode(1)
        a=head
        for i,j in di.items():
            if j==1:
                a.next=ListNode(i)
                a=a.next
        return head.next