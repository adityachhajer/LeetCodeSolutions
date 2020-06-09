# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            if root.left != None and root.left.left == None and root.left.right == None:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)




