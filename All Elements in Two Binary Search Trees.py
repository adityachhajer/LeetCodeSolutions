# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        if root1:
            k = [root1]
            while k:
                a = []
                for i in range(len(k)):
                    p = k.pop(0)
                    ans.append(p.val)
                    if p.left:
                        a.append(p.left)
                    if p.right:
                        a.append(p.right)
                k = a
        if root2:
            k = [root2]
            while k:
                a = []
                for i in range(len(k)):
                    p = k.pop(0)
                    ans.append(p.val)
                    if p.left:
                        a.append(p.left)
                    if p.right:
                        a.append(p.right)
                k = a
        ans.sort()
        return ans

