class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 0:
            return A
        x = []
        for i in range(len(A)):
            p = A[i]
            p = p[::-1]
            for i in range(len(p)):
                if p[i] == 0:
                    p[i] = 1
                else:
                    p[i] = 0
            x.append(p)
        return x

