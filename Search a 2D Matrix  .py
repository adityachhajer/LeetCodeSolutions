class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if target < matrix[i][j]:
                    return False
                if target == matrix[i][j]:
                    return True
        return False
