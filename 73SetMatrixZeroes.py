class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ii=[]
        jj=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    ii.append(i)
                    jj.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in ii or j in jj:
                    matrix[i][j]=0
        return matrix