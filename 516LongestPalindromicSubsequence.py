class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        m = len(s2) + 1
        n = len(s1) + 1
        l = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if s1[i - 1] == s2[j - 1]:
                    l[i][j] = 1 + l[i - 1][j - 1]
                else:
                    l[i][j] = max(l[i][j - 1], l[i - 1][j])
        return l[m - 1][n - 1]

