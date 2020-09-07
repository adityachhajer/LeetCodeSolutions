class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        def nonzeros(matrix):

            return [(i, j) for i, row in enumerate(matrix) for j, val in enumerate(row) if matrix[i][j]]

        acords = nonzeros(A)
        bcords = nonzeros(B)

        vectors_a_to_b = collections.Counter()
        for ax, ay in acords:
            for bx, by in bcords:
                vector = (bx - ax, by - ay)

                vectors_a_to_b[vector] += 1

        return max(vectors_a_to_b.values()) if vectors_a_to_b else 0