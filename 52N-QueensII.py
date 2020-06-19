class Solution:
    def totalNQueens(self, n):
        result = [0]

        def DFS(cos, xps, xms):
            i = len(cos)
            if i == n:
                result[0] += 1
                return
            for j in range(n):
                if j not in cos and i + j not in xps and i - j not in xms:
                    DFS(cos + [j], xps + [i + j], xms + [i - j])

        DFS([], [], [])
        return result[0]