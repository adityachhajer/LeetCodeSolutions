# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        result = 0

        def dfs(node=root):
            nonlocal result
            minval = maxval = node.val
            if node.left:
                lmin, lmax = dfs(node.left)
                minval = min(minval, lmin)
                maxval = max(maxval, lmax)
            if node.right:
                rmin, rmax = dfs(node.right)
                minval = min(minval, rmin)
                maxval = max(maxval, rmax)

            result = max(result, abs(node.val - minval), abs(node.val - maxval))
            return min(minval, node.val), max(maxval, node.val)

        dfs()

        return result
