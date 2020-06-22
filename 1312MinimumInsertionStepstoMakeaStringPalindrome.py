class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s[::]
        s2 = s[::-1]
        l = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    l[i][j] = 1 + l[i - 1][j - 1]
                else:
                    l[i][j] = max(l[i][j - 1], l[i - 1][j])
        return len(s1) - l[-1][-1]
