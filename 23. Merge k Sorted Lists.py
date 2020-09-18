# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = []
        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                l.append(cur.val)
                cur = cur.next
        l.sort()
        a = ListNode(0)
        cur = a
        while l:
            x = l.pop(0)
            cur.next = ListNode(x)
            cur = cur.next
        return a.next
