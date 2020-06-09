# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        else:
            a = self.helper(root.left, min, root.val)
            b = self.helper(root.right, root.val, max)
            return a and b
