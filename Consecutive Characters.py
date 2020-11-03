class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        c = 0
        ss = s[0]
        if len(s) <= 1:
            return 1
        a = len(s)
        i = 1
        while i < a:
            if s[i] == ss:
                ans += 1
            else:
                ss = s[i]
                c = max(ans, c)
                ans = 1

            i += 1
        c = max(ans, c)
        return c
