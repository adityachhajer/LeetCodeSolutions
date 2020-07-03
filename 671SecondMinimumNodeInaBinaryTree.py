# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        x=[]
        l=[root]
        while l:
            k=[]
            for i in l:
                x.append(i.val)
                if i.left:
                    k.append(i.left)
                if i.right:
                    k.append(i.right)
            l=k
        x=sorted(set(x))
        if len(x)==1:
            return -1
        return x[1]