# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        x=[]
        while head:
            x.append(head.val)
            head=head.next
        ans=[0 for _ in range(len(x))]
        stack=[0]
        ans=[0]*len(x)
        for i in range(1,len(x)):
            while stack and x[i]>x[stack[-1]]:
                ans[stack.pop()]=x[i]
            stack.append(i)
        return ans