# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        l = []
        x = 0
        summ = []
        while head:
            l.append(head.val)
            x = x + head.val
            if x in summ:
                a = summ.index(x)
                l = l[0:a + 1]
                summ = summ[0:a + 1]
            elif x == 0:
                l = []
                summ = []
            else:
                summ.append(x)
            head = head.next

        a = ListNode(0)
        head = a
        for i in l:
            head.next = ListNode(i)
            head = head.next
        return a.next