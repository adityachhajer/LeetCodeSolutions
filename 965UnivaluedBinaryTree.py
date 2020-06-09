# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        k = [root.val]
        stack = [root]
        while stack:
            a = stack.pop(0)
            if a.left:
                if a.left.val in k:
                    stack.append(a.left)
                else:
                    return False
            if a.right:
                if a.right.val in k:
                    stack.append(a.right)
                else:
                    return False
        return True

