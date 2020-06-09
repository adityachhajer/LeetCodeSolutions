class Solution:
    def summ(self, l, i, j, m, n, k):
        if i == m - 1 and j == n - 1:
            return l[i][j]
        if k[i][j] != 0:
            return k[i][j]
        else:
            if i == m - 1:
                k[i][j] = l[i][j] + self.summ(l, i, j + 1, m, n, k)
                return k[i][j]
            if j == n - 1:
                k[i][j] = l[i][j] + self.summ(l, i + 1, j, m, n, k)
                return k[i][j]
            else:
                k[i][j] = min(l[i][j] + self.summ(l, i + 1, j, m, n, k), l[i][j] + self.summ(l, i, j + 1, m, n, k))
                return k[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        k = [[0 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        return self.summ(grid, 0, 0, len(grid), len(grid[0]), k)
