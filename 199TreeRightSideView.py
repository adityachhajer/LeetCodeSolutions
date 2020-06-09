# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        value = []
        q = []
        c = []
        q.append(root)
        while (len(q)):
            n = len(q)
            for i in range(1, n + 1):
                t = q[0]
                q.pop(0)
                if i == n:
                    c.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
        return c


