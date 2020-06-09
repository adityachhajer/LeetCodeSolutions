class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l=[[0 for _ in range(n+1)]for _ in range(m+1)]
        l[0][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                l[i][j]=l[i-1][j]+l[i][j-1]
        return l[m][n]