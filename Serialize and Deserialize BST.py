class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ""
        paths = []

        def dfs(node):
            nonlocal paths
            if not node:
                paths.append('#')
                return
            paths.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(paths)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return []
        idx = 0
        data_list = data.split(',')

        def dfs_preorder(data_list):
            nonlocal idx
            if idx >= len(data_list):
                return None

            val = data_list[idx]
            idx += 1

            if val == '#':
                return None

            root = TreeNode(val)
            root.left = dfs_preorder(data_list)
            root.right = dfs_preorder(data_list)
            return root

        return dfs_preorder(data_list)