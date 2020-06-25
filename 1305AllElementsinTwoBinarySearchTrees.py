# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if root1 == None and root2 == None:
            return []
        if root1 == None and root2 != None:
            l = []
            x = [root2]
            while x:
                t = []
                for i in x:
                    l.append(i.val)
                    if i.left:
                        t.append(i.left)
                    if i.right:
                        t.append(i.right)
                x = t
            return sorted(l)
        if root1 != None and root2 == None:
            l = []
            x = [root1]
            while x:
                t = []
                for i in x:
                    l.append(i.val)
                    if i.left:
                        t.append(i.left)
                    if i.right:
                        t.append(i.right)
                x = t
            return sorted(l)

        l = []
        x = [root1]
        while x:
            t = []
            for i in x:
                l.append(i.val)
                if i.left:
                    t.append(i.left)
                if i.right:
                    t.append(i.right)
            x = t
        x = [root2]
        while x:
            t = []
            for i in x:
                l.append(i.val)
                if i.left:
                    t.append(i.left)
                if i.right:
                    t.append(i.right)
            x = t
        return sorted(l)
