class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            k = ''
            p = ''
            for j in range(i, len(s)):
                k = k + s[j]
                p = s[j] + p
                if k == p:
                    c = c + 1

        return c