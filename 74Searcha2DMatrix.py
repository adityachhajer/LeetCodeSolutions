class Solution:
    def solve(self,matrix,target):
        for i in matrix:
            for j in i:
                if j > target:
                    return False
                else:
                    if j==target:
                        return True
                    else:
                        if j>target:
                            return False
                        continue
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.solve(matrix,target)