# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxle=0
        if root==None:
            return 0
        l=[root]
        c=0
        prev=float('-inf')
        while l:
            maxle+=1
            a=[]
            b=[]
            for i in range(len(l)):
                x=l.pop()
                a.append(x.val)
                if x.left:
                    b.append(x.left)
                if x.right:
                    b.append(x.right)
            if sum(a)>prev:
                c=maxle
                prev=sum(a)
            l=b
        return c