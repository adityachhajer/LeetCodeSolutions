class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    l[i][j] = 1 + l[i - 1][j - 1]
                else:
                    l[i][j] = max(l[i - 1][j], l[i][j - 1])
        if l[len(s)][len(t)] == len(s):
            return True
        else:
            return False
