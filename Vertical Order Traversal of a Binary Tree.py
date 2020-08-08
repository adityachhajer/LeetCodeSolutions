# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
	    d = collections.defaultdict(list)

	    def dfs(node, m, n):
		    d[m].append([n, node.val])
		    if node.left: dfs(node.left, m-1, n+1)
		    if node.right: dfs(node.right, m+1, n+1)

	    dfs(root, 0, 0)
	    return [[v[1] for v in sorted(d[k])] for k in sorted(d)]