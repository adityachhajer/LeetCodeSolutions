# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = []
        stack.append(root.val)
        a = [root]
        while a:
            x = a.pop(0)
            if x.left:
                stack.append(x.left.val)
                a.append(x.left)

            if x.right:
                stack.append(x.right.val)
                a.append(x.right)
        stack.sort()
        b = stack.index(L)
        c = stack.index(R)
        return sum(stack[b:c + 1])

