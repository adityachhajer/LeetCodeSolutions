class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        """
        Do not return anything, modify matrix in-place instead.
        """
