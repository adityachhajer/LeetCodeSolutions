# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        k = []
        while head:
            k.append(head.val)
            head = head.next
        l = list(k)
        l.reverse()
        if k == l:
            return True
        return False

