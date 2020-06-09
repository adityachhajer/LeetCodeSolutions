# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         t = [[-1 for _ in range(1001)] for _ in range(1001)]
#         return self.LCS(text1, text2, len(text1), len(text2), t)
#
#     def LCS(self, s1, s2, n, m, t):
#         if n == 0 or m == 0:
#             return 0
#         if t[n][m] != -1:
#             return t[n][m]
#         else:
#             if s1[n - 1] == s2[m - 1]:
#                 t[n][m] = 1 + self.LCS(s1, s2, n - 1, m - 1, t)
#                 return t[n][m]
#             else:
#                 t[n][m] = max(self.LCS(s1, s2, n - 1, m, t), self.LCS(s1, s2, n, m - 1, t))
#                 return t[n][m]
#


# efficient solution:


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = text1
        s2 = text2
        m = len(s1) + 1
        n = len(s2) + 1
        l = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    l[i][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if s1[i - 1] == s2[j - 1]:
                    l[i][j] = 1 + l[i - 1][j - 1]
                else:
                    l[i][j] = max(l[i][j - 1], l[i - 1][j])
        return l[m - 1][n - 1]

