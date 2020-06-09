class Solution:
    def findmin(self, triangle, k, i, sum, t):
        if k >= len(triangle) or i >= len(triangle[k]):
            return 0
        if t[k][i] != -1:
            return t[k][i]
        t[k][i] = sum = triangle[k][i] + min(self.findmin(triangle, k + 1, i, sum, t),
                                             self.findmin(triangle, k + 1, i + 1, sum, t))
        return sum

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        t = [[-1 for _ in range(len(triangle[-1]) + 1)] for j in range(len(triangle) + 1)]
        return self.findmin(triangle, 0, 0, sum, t)