# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rota(self, head, p):
        if p == 0:
            return head
        x = head
        cur = head
        prev = cur
        while (cur.next != None):
            prev = cur
            cur = cur.next
        prev.next = None
        cur.next = x
        head = cur
        return self.rota(head, p - 1)

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        if k == 0:
            return head
        if head.next == None:
            return head
        c = 0
        cur = head
        while cur.next != None:
            c = c + 1
            cur = cur.next
        c = c + 1
        if k > c:
            p = k % c
        else:
            p = k
        return self.rota(head, p)





