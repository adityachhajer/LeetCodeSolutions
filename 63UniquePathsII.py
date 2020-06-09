class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        l = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        l[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    l[i][j] = 0
                else:
                    l[i][j] = l[i - 1][j] + l[i][j - 1]
        return l[m][n]


