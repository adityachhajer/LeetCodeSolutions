class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum = 0
        i = 5
        while (n / i >= 1):
            sum += n // i
            i *= 5
        return sum



