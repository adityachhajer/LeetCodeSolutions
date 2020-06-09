# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helpe(self, root):
        if root is None:
            return 1
        l = self.helpe(root.left)
        r = self.helpe(root.right)
        if abs(l - r) <= 1 and l and r:
            return 1 + max(l, r)
        else:
            return False

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helpe(root)
