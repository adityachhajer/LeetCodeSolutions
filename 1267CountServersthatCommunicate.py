class Solution:
    def check(self, grid, n, x, i, j, k):
        if k == 0:
            while i >= 0:
                if grid[i][j] == 1:
                    return True
                i -= 1
            return False
        if k == 1:
            while i <= n - 1:
                if grid[i][j] == 1:
                    return True
                i += 1
            return False
        if k == 2:
            while j >= 0:
                if grid[i][j] == 1:
                    return True
                j -= 1
            return False
        if k == 3:
            while j <= x - 1:
                if grid[i][j] == 1:
                    return True
                j += 1
            return False

    def solve(self, grid, n, x, c):
        a = False
        for i in range(n):
            for j in range(x):
                if grid[i][j] == 1:
                    a = self.check(grid, n, x, i - 1, j, 0) or self.check(grid, n, x, i + 1, j, 1) or self.check(grid,n, x,i,j - 1,2) or self.check(grid, n, x, i, j + 1, 3)
                    if a == True:
                        c = c + 1
                    a = False
        return c

    def countServers(self, grid: List[List[int]]) -> int:
        c = 0
        return self.solve(grid, len(grid), len(grid[0]), c)
