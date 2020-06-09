class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.ans =  max(self.ans, left + right)
            return max(left,right) + 1
        helper(root)
        return self.ans