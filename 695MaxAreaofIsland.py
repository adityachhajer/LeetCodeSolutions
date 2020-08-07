class Solution:
    def solve(self,grid,i,j):
        grid[i][j]=0
        x=0
        y=0
        z=0
        t=0
        if i+1<len(grid):
            if grid[i+1][j]==1:
                x=self.solve(grid,i+1,j)
        if i-1>=0:
            if grid[i - 1][j] == 1:
                y = self.solve(grid, i - 1, j)
        if j+1<len(grid[0]):
            if grid[i ][j+1] == 1:
                z = self.solve(grid, i , j + 1)
        if j - 1 >= 0:
            if grid[i ][j - 1] == 1:
                t = self.solve(grid, i, j - 1)
        return 1+x+y+z+t

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==0:
                    continue
                else:
                    x=self.solve(grid,i,j)
                    ans=max(ans,x)
        return ans