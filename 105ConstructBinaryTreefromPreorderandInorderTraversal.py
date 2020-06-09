# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.bst(preorder, inorder)

    def bst(self, preorder, inorder):
        lenpre = len(preorder)
        lenin = len(inorder)
        if lenpre != lenin or lenpre == 0 or preorder == None or inorder == None:
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)

        root.left = self.bst(preorder[1:rootindex + 1], inorder[:rootindex])
        root.right = self.bst(preorder[rootindex + 1:], inorder[rootindex + 1:])
        return root