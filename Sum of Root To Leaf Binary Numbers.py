# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def selff(self, ans, root, l):
        if root == None:
            return
        ans = ans + str(root.val)
        # print(ans)
        if root.left is None and root.right is None:
            l.append(int(ans, 2))
            return
        if root.left:
            self.selff(ans, root.left, l)
        if root.right:
            self.selff(ans, root.right, l)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root == None:
            return 0
        ans = ''
        l = []
        self.selff(ans, root, l)
        return sum(l)