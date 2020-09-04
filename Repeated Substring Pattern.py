class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ans = ''
        if len(s) == 1:
            return False

        a = 0
        k = len(s) // 2
        k += 1
        while a < k:
            ans = ans + s[a]
            c = s.count(ans)
            p = c * len(ans)
            if p == len(s):
                return True
            a = a + 1
        return False