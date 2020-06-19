class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [False]*(n)
        diag1 = [False]*(2*n)
        diag2 = [False]*(2*n)
        ans = []
        def backTrack(y,grid=[]):
            if(y==n):
                ans.append(grid[:])
            else:
                for x in range(0,n):
                    if(col[x] or diag1[x+y] or diag2[x-y+n-1]):continue
                    col[x],diag1[x+y],diag2[x-y+n-1]=1,1,1
                    tempGrid = ['.']*(n)
                    tempGrid[x] = 'Q'
                    grid.append("".join(tempGrid))
                    backTrack(y+1)
                    col[x],diag1[x+y],diag2[x-y+n-1]=0,0,0
                    grid.pop()
        backTrack(0)
        return ans