# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float('-inf')

    def solve(self, root, res):
        if root == None:
            return 0
        l = self.solve(root.left, self.res)
        r = self.solve(root.right, self.res)

        temp = max((max(l, r) + root.val), root.val)
        ans = max(temp, root.val + l + r)
        self.res = max(self.res, ans)
        return temp

    def maxPathSum(self, root: TreeNode) -> int:
        self.solve(root, self.res)
        return self.res