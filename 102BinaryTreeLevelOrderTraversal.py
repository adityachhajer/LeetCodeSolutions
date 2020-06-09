# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        l=[]
        k=[root]
        while (k):
            g=[]
            n=len(k)
            c=[]
            for i in k:
                g.append(i.val)
                if i.left:
                    c.append(i.left)
                if i.right:
                    c.append(i.right)
            l.append(g)
            k=c
        return l