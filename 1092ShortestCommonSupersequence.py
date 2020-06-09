class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1) + 1
        n = len(str2) + 1
        l = [[0 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if str1[i - 1] == str2[j - 1]:
                    l[i][j] = 1 + l[i - 1][j - 1]
                else:
                    l[i][j] = max(l[i][j - 1], l[i - 1][j])
        i = m - 1
        j = n - 1
        res = ''
        while (i > 0 and j > 0):
            if str1[i - 1] == str2[j - 1]:
                res = str1[i - 1] + res
                j -= 1
                i -= 1
            else:
                if l[i][j - 1] > l[i - 1][j]:
                    res = str2[j - 1] + res
                    j -= 1
                else:
                    res = str1[i - 1] + res
                    i -= 1
        while (i > 0):
            res = str1[i - 1] + res
            i -= 1
        while (j > 0):
            res = str2[j - 1] + res
            j -= 1
        return res

