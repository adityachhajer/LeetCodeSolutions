# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, l):
        if root is None:
            return None
        l.append(root.val)
        if root.left:
            self.solve(root.left, l)
        if root.right:
            self.solve(root.right, l)
        return None

    def findTarget(self, root: TreeNode, k: int) -> bool:
        l = []
        self.solve(root, l)
        for i in range(len(l)):
            x = k - l[i]
            if x in l[i + 1:]:
                return True
        return False
