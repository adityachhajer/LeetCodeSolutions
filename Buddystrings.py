class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B and len(A) - len(set(A)) >= 1:
            return True
        dif = []
        for i in range(len(A)):
            if A[i] != B[i]:
                dif.append(i)
                if (len(dif)) > 2:
                    return False

        if len(dif) != 2:
            return False

        if A[dif[0]] == B[dif[1]] and A[dif[1]] == B[dif[0]]:
            return True
        return False