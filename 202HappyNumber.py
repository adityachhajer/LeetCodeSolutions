class Solution:
    def isHappy(self, n: int) -> bool:
        c = 0
        while (n > 0):
            a = n % 10
            c = c + (a ** 2)
            n = n // 10
        if c == 1:
            return True
        elif c == 4:
            return False
        else:
            return self.isHappy(c)

