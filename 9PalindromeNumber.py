class Solution:
    def isPalindrome(self, x: int) -> bool:
        t = x
        rem = 0
        while (x > 0):
            a = x % 10
            rem = rem * 10 + a
            x = x // 10
        if rem == t:
            return True
        else:
            return False
