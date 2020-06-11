class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex + 1
        l = [[0 for j in range(0, i)] for i in range(1, n + 1)]
        for i in range(n):
            l[i][i] = 1
            l[i][0] = 1
        for i in range(n):
            for j in range(len(l[i])):
                if j == 0 or i == j:
                    continue
                else:
                    l[i][j] = l[i - 1][j] + l[i - 1][j - 1]
        return l[-1]
