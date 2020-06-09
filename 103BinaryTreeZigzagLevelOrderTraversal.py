# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        l = []
        k = [root]
        t = 0
        while (k):
            g = []
            m = []
            for i in k:
                g.append(i.val)
                if i.left:
                    m.append(i.left)
                if i.right:
                    m.append(i.right)

            if t % 2 != 0:
                g = reversed(g)
            k = m
            l.append(g)
            t += 1
        return l