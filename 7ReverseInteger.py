class Solution:
    def reverse(self, x: int) -> int:
        if x > 2147483647 or x < -2147483648:
            return 0
        elif x >= 0:
            test = str(x)
            test2 = test[::-1]
        else:
            test = str(abs(x))
            test = test + ('-')
            test2 = test[::-1]
        if int(test2) > 2147483647 or int(test2) < -2147483648:
            return 0
        else:

            return int(test2)

