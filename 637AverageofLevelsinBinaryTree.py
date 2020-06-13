# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        l = []
        t = [root]
        while t:
            n = len(t)
            k = []
            c = 0
            for i in t:
                c = c + i.val
                if i.left:
                    k.append(i.left)
                if i.right:
                    k.append(i.right)
            s = float(c / n)
            l.append(s)
            t = k
        return l
