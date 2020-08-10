# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, sum):
        if not root:
            return 0
        if root.val == sum:
            return 1 + self.helper(root.left, sum - root.val) + self.helper(root.right, sum - root.val)
        return self.helper(root.left, sum - root.val) + self.helper(root.right, sum - root.val)

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
