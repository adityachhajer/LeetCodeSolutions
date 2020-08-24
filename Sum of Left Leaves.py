# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans=0
        data=[root]
        while data:
            x=[]
            for i in range(len(data)):
                a=data.pop(0)
                if a.left:
                    if not a.left.left and not  a.left.right:
                        ans+=a.left.val
                    x.append(a.left)
                if a.right:
                    x.append(a.right)
            data=x
        return ans