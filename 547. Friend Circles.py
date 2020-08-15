class Solution:
    def solve(self, j, M):
        for i in range(len(M[0])):
            if M[j][i] == 1:
                M[i][j], M[j][i] = 0, 0
                self.solve(i, M)
        return M

    def findCircleNum(self, M: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    cnt += 1
                    M[i][j], M[j][i] = 0, 0
                    self.solve(j, M)
        return cnt