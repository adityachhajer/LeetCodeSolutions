class Solution:
    def titleToNumber(self, s: str) -> int:
        x = len(s) - 1
        summ = 0
        for i in s:
            summ += (26 ** x) * (ord(i) - ord('A') + 1)
            x = x - 1
        return summ
