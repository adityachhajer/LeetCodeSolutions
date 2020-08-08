class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        roots = set(range(n))
        for c in leftChild + rightChild:
            if c == -1:
                continue
            if c not in roots:
                return False
            roots.remove(c)

        if len(roots) != 1:
            return False

        def dfs(root: int) -> int:
            if root == -1:
                return 0
            return 1 + dfs(leftChild[root]) + dfs(rightChild[root])

        return dfs(roots.pop()) == n