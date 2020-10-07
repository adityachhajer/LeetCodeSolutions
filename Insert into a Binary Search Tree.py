# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, mainroot, val):
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
                return mainroot
            else:
                return self.solve(root.right, mainroot, val)
        else:
            if root.left == None:
                root.left = TreeNode(val)
                return mainroot
            else:
                return self.solve(root.left, mainroot, val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode(val)
            return root
        if root.left == None and root.right == None:
            if val < root.val:
                root.left = TreeNode(val)
            else:
                root.right = TreeNode(val)
            return root
        return self.solve(root, root, val)
