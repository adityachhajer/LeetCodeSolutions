class Solution:
    def dfs(self, grid, i, j, c):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1):
            return 0
        if (grid[i][j] == 2):
            if c == -1:
                return 1
            else:
                return 0
        grid[i][j] = -1
        c -= 1
        tp = self.dfs(grid, i + 1, j, c) + self.dfs(grid, i - 1, j, c) + self.dfs(grid, i, j + 1, c) + self.dfs(grid, i,
                                                                                                                j - 1,
                                                                                                                c)
        grid[i][j] = 0
        c += 1
        return tp

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        c = 0
        x = 0
        y = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    c += 1
                elif grid[i][j] == 1:
                    x = i
                    y = j
        return self.dfs(grid, x, y, c)