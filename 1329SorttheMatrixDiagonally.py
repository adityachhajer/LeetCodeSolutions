from collections import defaultdict
from queue import PriorityQueue
class Solution:
    def diagonalSort(self, mat):
        diags = defaultdict(PriorityQueue)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                diags[i-j].put(mat[i][j])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = diags[i-j].get()
        return ans