# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self, root, p, q):
        if not root:
            return False

        c = 0

        left = self.solve(root.left, p, q)
        right = self.solve(root.right, p, q)
        mid = root == p or root == q
        if mid == True:
            c = c + 1
        if left == True:
            c = c + 1
        if right == True:
            c = c + 1
        if c >= 2:
            return root
        return mid or left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        return self.solve(root, p, q)